from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Dish, Cuisine, Category, Ingredient
from django.forms.models import model_to_dict
from django.db.models import Q # Support for 'OR' chain in query
import csv
import io # For PDF Generation
from reportlab.pdfgen import canvas 
import unicodedata

# Create your views here.
def fullmenu(request):
    # dishes = list(Dish.objects.values())
    # return JsonResponse({'menu':dishes})
    # #return HttpResponse("This is the endpoint to return the full menu.")
    dishes = []
    items = Dish.objects.all()
    for item in items:
        dishes.append({
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "spicy_level": item.spicy_level,
            "cuisine": {
                "title": item.cuisine.title
            },
            "category": {
                "title": item.category.title
            },
            "ingredients": {
                "title": list(item.ingredient.values())
            },
            # "cuisine": (Cuisine.objects.get(id=item.cuisine_id)),
            # "category": (Category.objects.get(id=item.category_id)),
        })
    #print(dishes)
    return JsonResponse(dishes, safe=False)

def appetizers(request):
    apps = list(Dish.objects.filter(category=1).values())
    return JsonResponse(apps, safe=False)
    # return HttpResponse("This is the appetizer list.")

def breakfast(request):
    breakfast = list(Dish.objects.filter(category=2).values())
    return JsonResponse(breakfast, safe=False)

def brunch(request):
    brunch = list(Dish.objects.filter(category=3).values())
    return JsonResponse(brunch, safe=False)

def lunch(request):
    lunch = list(Dish.objects.filter(category=4).values())
    return JsonResponse(lunch, safe=False)

def dinner(request):
    dinner = list(Dish.objects.filter(category=5).values())
    return JsonResponse(dinner, safe=False)

def sides(request):
    sides = list(Dish.objects.filter(category=6).values())
    return JsonResponse(sides, safe=False)

def desserts(request):
    desserts = list(Dish.objects.filter(category=7).values())
    return JsonResponse(desserts, safe=False)

def eggdishes(request):
    htmlinsert = ""
    eggdishes = list(Dish.objects.filter(ingredient=1).all())
    for item in eggdishes:
        htmlinsert = htmlinsert + "<li>" + str(item.title) + "</li>"
    html = """
    <html>
    <body>
        <h1>These Dishes Contain Egg or Egg Products:</h1>
        <ul> 
            %s 
        </ul>
    </body>
    </html>""" % htmlinsert
    return HttpResponse(html)

def dairy(request):
    htmlinsert = ""
    dairy = list(Dish.objects.filter(Q(ingredient=2) | Q(ingredient=3) | Q(ingredient=8)).all())
    for item in dairy:
        htmlinsert = htmlinsert + "<li>" + str(item.title) + "</li>"
    html = """
    <html>
    <body>
        <h1>These Dishes Contain Dairy:</h1>
        <ul> 
            %s 
        </ul>
    </body>
    </html>""" % htmlinsert
    return HttpResponse(html)
    # dairy = list(Dish.objects.filter(Q(ingredient=2) | Q(ingredient=3) | Q(ingredient=8)).values())
    # return JsonResponse(dairy, safe=False)

def menu_to_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="gitgrub-menu.csv"'},
    )

    menu = list(Dish.objects.values())
    writer = csv.writer(response)
    for dish in menu:
        writer.writerow(dish.values())
    return response

def menu_to_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    menu = list(Dish.objects.values())
    for dish in menu:
        # uniLine = str(dish, 'latin-1')
        p.drawString(100, 100, str(dish.values()))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='gitgrub-menu.pdf')
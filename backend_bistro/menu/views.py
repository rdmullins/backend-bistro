from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Dish, Cuisine, Category, Ingredient
from django.forms.models import model_to_dict
from django.db.models import Q

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
                "title": item.cuisine_id.title
            },
            "category": {
                "title": item.category_id.title
            },
            "ingredients": {
                "title": list(item.ingredient_id.values())
            },
            # "cuisine": (Cuisine.objects.get(id=item.cuisine_id)),
            # "category": (Category.objects.get(id=item.category_id)),
        })
    #print(dishes)
    return JsonResponse(dishes, safe=False)

def appetizers(request):
    apps = list(Dish.objects.filter(category_id=1).values())
    return JsonResponse(apps, safe=False)
    # return HttpResponse("This is the appetizer list.")

def breakfast(request):
    breakfast = list(Dish.objects.filter(category_id=2).values())
    return JsonResponse(breakfast, safe=False)

def brunch(request):
    brunch = list(Dish.objects.filter(category_id=3).values())
    return JsonResponse(brunch, safe=False)

def lunch(request):
    lunch = list(Dish.objects.filter(category_id=4).values())
    return JsonResponse(lunch, safe=False)

def dinner(request):
    dinner = list(Dish.objects.filter(category_id=5).values())
    return JsonResponse(dinner, safe=False)

def sides(request):
    sides = list(Dish.objects.filter(category_id=6).values())
    return JsonResponse(sides, safe=False)

def desserts(request):
    desserts = list(Dish.objects.filter(category_id=7).values())
    return JsonResponse(desserts, safe=False)

def eggdishes(request):
    eggdishes = list(Dish.objects.filter(ingredient_id=1).values())
    return JsonResponse(eggdishes, safe=False)

def dairy(request):
    dairy = list(Dish.objects.filter(Q(ingredient_id=2) | Q(ingredient_id=3) | Q(ingredient_id=8)).values())
    return JsonResponse(dairy, safe=False)
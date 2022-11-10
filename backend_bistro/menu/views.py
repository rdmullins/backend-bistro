from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Dish, Cuisine, Category
from django.forms.models import model_to_dict

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
            # "cuisine": (Cuisine.objects.get(id=item.cuisine_id)),
            # "category": (Category.objects.get(id=item.category_id)),
        })
    print(dishes)
    return JsonResponse(dishes, safe=False)
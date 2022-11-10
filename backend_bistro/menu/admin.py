from django.contrib import admin
from .models import Dish, Cuisine, Category
# Register your models here.
admin.site.register(Dish)
admin.site.register(Cuisine)
admin.site.register(Category)
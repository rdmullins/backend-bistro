from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.title)

class Cuisine(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.title)

class Ingredient(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.title)

class Dish(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    spicy_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return 'Title: %s, Desc.: %s, Price: $%s, Spice Level: %s, Category: %s, Cuisine: %s' % (self.title, self.description, self.price, self.spicy_level, self.category.title, self.cuisine.title)

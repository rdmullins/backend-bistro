# Generated by Django 4.1.3 on 2022-11-10 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_ingredient_dish_ingredient_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='cuisine_id',
            new_name='cuisine',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
    ]

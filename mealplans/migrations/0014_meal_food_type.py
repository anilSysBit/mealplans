# Generated by Django 5.1.2 on 2024-12-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplans', '0013_meal_calories_meal_carbs_meal_fats_meal_protein'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='food_type',
            field=models.CharField(choices=[('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Non-Veg', 'Non-Veg')], default='Non-Veg', max_length=20),
            preserve_default=False,
        ),
    ]
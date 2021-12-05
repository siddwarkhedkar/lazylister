from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Meals

import random
import urllib.parse


def index(request):
    return render(request, 'lister/index.html')


def random_list(request):
    meal_names, shopping_list = ([] for i in range(2))
    all_meals = Meals.objects.all()

    for meal in all_meals:
        meal_names.extend(meal.name.split(","))

    random_meals = random.sample(meal_names, 3)

    for item in all_meals:
        if item.name in random_meals:
            shopping_list.extend(item.ingredients.split(","))

    shopping_list = list(set(shopping_list))

    context = {
        "random_meals": random_meals,
        "all_ingredients": shopping_list
    }

    return render(request, 'lister/random.html', context)


def meals(request):
    all_meals = Meals.objects.all()

    context = {
        'all_meals': all_meals
    }

    return render(request, 'lister/meals.html', context)


def ingredients_list(request, meal_name):
    meal = get_object_or_404(Meals, name=urllib.parse.unquote_plus(meal_name))
    context = {}
    if meal.ingredients:
        context = {
            "ingredients": meal.ingredients.split(",")
        }

    return render(request, 'lister/ingredients.html', context)


def add_meal(request):
    return render(request, 'lister/addmeal.html')


def new_meal(request):
    name, ingredients = None, None
    if request.method == "POST":
        name = request.POST.get("name")
        ingredients = request.POST.get("ingredients")

    new = Meals(name=name, ingredients=ingredients)
    new.save()

    return render(request, 'lister/success.html')


def remove_meal(request):
    meal_to_delete = get_object_or_404(Meals, id=request.POST.get("delete-meal-id"))

    try:
        meal_to_delete.delete()
    except:
        return HttpResponse("Your request to delete couldn't be completed")
    else:
        return render(request, 'lister/success.html')

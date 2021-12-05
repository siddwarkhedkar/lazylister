from django.urls import path

from . import views

app_name = 'lister'
urlpatterns = [
    path('', views.index, name='index'),
    path('meals/', views.meals, name='meals'),
    path('meals/<str:meal_name>/', views.ingredients_list, name='ingredient_list'),
    path('add-meal/', views.add_meal, name="add_meal"),
    path('add-meal/new', views.new_meal, name="new_meal"),
    path('remove', views.remove_meal, name="remove_meal"),
    path('random', views.random_list, name="random_list")
]
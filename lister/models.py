from django.db import models

# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(blank=True)

    def __str__(self):
        return self.name

from django.contrib import admin
from . import models

admin.site.register(models.MealAlbum)
admin.site.register(models.Category)
admin.site.register(models.Units)
admin.site.register(models.Meal)
admin.site.register(models.Comments)
admin.site.register(models.Order)
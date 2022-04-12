from django.db import models
from django.contrib.auth.models import User
from helpers.models import Base


class MealPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to='menu/meals/')


class Category(Base):
    ...


class Units(Base):
    ...


class Meal(Base):
    photos = models.ManyToManyField(MealPhoto, blank=True, verbose_name='Альбом')
    price = models.PositiveIntegerField("Цена")
    description = models.CharField("Описание", max_length=512)
    size = models.PositiveIntegerField("Порция кол-во")
    units = models.ForeignKey(Units, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Единица Измерения')


class Comments(Base):
    meal = models.ForeignKey(Meal, verbose_name='Блюда', on_delete=models.CASCADE, blank=True, null=True)


from django.db import models
from django.contrib.auth.models import User
from helpers.models import Base
from restaurant.models import RestaurantAddress


class Category(Base):
    ...


class Units(Base):
    ...


class MealAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to='menu/meals/')
    main = models.BooleanField("Главное фото", default=False)


class Meal(Base):
    address = models.ForeignKey(RestaurantAddress, on_delete=models.CASCADE, verbose_name='Адресс доставки')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='Категории')
    price = models.PositiveIntegerField("Цена")
    description = models.CharField("Описание", max_length=512)
    size = models.PositiveIntegerField("Порция кол-во")
    units = models.ForeignKey(Units, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Единица Измерения')
    album = models.ManyToManyField(MealAlbum, blank=True, verbose_name='Альбом фотографий')


class Comments(Base):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, verbose_name='Блюда', on_delete=models.CASCADE, blank=True, null=True)




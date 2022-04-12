from django.db import models
from django.contrib.auth.models import User

from helpers.models import Base, Location


class Restaurant(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ответственный человек')
    name = models.CharField("Название ресторана", max_length=128)
    phone = models.CharField("Номер телефона", max_length=16)


class RestaurantAddress(Base):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="Ресторан")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    name = models.CharField('Название отделения', max_length=128)






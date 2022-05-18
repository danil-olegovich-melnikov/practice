from django.db import models
from django.contrib.auth.models import User
from helpers.models import Base
from company.models import CompanyAddress


class Category(Base):
    ...


class Units(Base):
    ...


class MealAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to='menu/meals/')
    main = models.BooleanField("Главное фото", default=False)


class Meal(Base):
    address = models.ForeignKey(CompanyAddress, on_delete=models.CASCADE, verbose_name='Адресс доставки')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='Категории')
    price = models.PositiveIntegerField("Цена")
    description = models.CharField("Описание", max_length=512)
    size = models.PositiveIntegerField("Порция кол-во")
    units = models.ForeignKey(Units, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Единица Измерения')
    album = models.ManyToManyField(MealAlbum, blank=True, verbose_name='Альбом фотографий')

    class Meta:
        ordering =['id']

class Comments(Base):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, verbose_name='Блюда', on_delete=models.CASCADE, blank=True, null=True)


class Order(models.Model):
    created_date = models.DateField(auto_now=True)
    delivery_date = models.DateField("Дата заказа")
    time_delivery = models.CharField("Время доставки", max_length=5,
                                     choices=(
                                         ("9:00", "9:00"),
                                         ("12:00", "12:00"),
                                         ("15:00", "15:00"),
                                     ))
    name = models.CharField("ФИО", max_length=256, blank=True)
    phone = models.CharField("Способ связи", max_length=256, blank=True)
    address = models.CharField("Адрес", max_length=256, blank=True)
    description = models.CharField("Описание", max_length=1024, blank=True)
    meals = models.ManyToManyField(Meal)
    user = models.ForeignKey(CompanyAddress, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.PositiveIntegerField("Общая стоимость", default=0)

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return f"Заказ: {self.id}"
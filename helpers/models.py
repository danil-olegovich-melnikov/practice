from django.db import models


class Base(models.Model):
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    name = models.CharField("Название", max_length=128)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

    class Meta:
        abstract = True


class Location(Base):
    name = models.CharField('Адрес', max_length=120)


class Form(Base):
    type = models.CharField(
        "Тип",
        choices=(("restaurant", "Ресторан"), ("worker", "Курьер"), ("company", "Компания")),
        max_length=100,
    )
    contact = models.CharField("Способ связи", max_length=256)
    description = models.CharField("Описание", max_length=512)


class Faqs(Base):
    description = models.CharField("FAQS", max_length=256)

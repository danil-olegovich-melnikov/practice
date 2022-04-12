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

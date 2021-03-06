from django.db import models
from helpers.models import Base
from django.contrib.auth.models import User
from helpers.models import Location


# Create your models here.
class Phone(Base):
    ...


class Company(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Администратор')
    phones = models.ManyToManyField(Phone, verbose_name='Телефона')
    description = models.CharField("Описание", max_length=512, blank=True)
    location = models.CharField("Адрес", max_length=512)
    image = models.ImageField("Обложка", upload_to="company/cover/", blank=True)
    role = models.CharField(
        "Роль",
        max_length=20,
        choices=(("restaurant", "restaurant"), ("company", "company"))
    )

    def is_restaurant(self) -> bool:
        return self.role == "restaurant"

    def is_company(self) -> bool:
        return self.role == "company"


class CompanyAddress(Base):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    phones = models.ManyToManyField(Phone, verbose_name='Номер точки')




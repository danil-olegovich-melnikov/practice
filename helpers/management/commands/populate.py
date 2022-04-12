from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from helpers import models as models_helpers
from menu import models as models_menu
from restaurant import models as models_restaurant


class Command(BaseCommand):
    help = 'Populate the database'

    @staticmethod
    def populate():
        user1 = User(username="user", first_name="Данил", last_name="Мельников", is_superuser=True, is_staff=True)
        user1.set_password('1234')
        user1.save()
        #others

        location1 = models_helpers.Location(name='МЕГА, Розыкабиева')
        location1.save()
        #others

        restaurant1 = models_restaurant.Restaurant(name='Лагман Сити', phone='+7700000000', user=user1)
        restaurant1.save()
        # others

        restaurant_address1 = models_restaurant.RestaurantAddress(name='Точка 1', location=location1, restaurant=restaurant1)
        restaurant_address1.save()
        # others

        category1 = models_menu.Category(name='Жаренное')
        category1.save()
        # others

        unit1 = models_menu.Units(name='грамм').save()
        # others

        meal1 = models_menu.Meal(
            name='Лагман',
            price=1000,
            description='Вкусный лагман с бараниной',
            size=300,
            units=unit1,
            address=restaurant_address1,
        )
        meal1.save()
        meal1.categories.add(category1)
        # others

        models_menu.Comments(meal=meal1, name='Заказывал лагман, мне очень понравилось, много мяса', user=user1).save()
        #others

    def handle(self, *args, **options):
        if User.objects.filter(username='user').exists():
            self.stdout.write('DB was populated before')
            return

        self.populate()

        self.stdout.write(self.style.SUCCESS('Successfully populated'))

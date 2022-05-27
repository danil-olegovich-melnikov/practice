import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from helpers import models as models_helpers
from menu import models as models_menu
from company import models as models_company
from faker import Faker

faker = Faker("ru_RU")


description_rest = """
<h3>ОмНом - лучшая восточная стрит еда во всем городе!💯</h3>

<p>Самый вкусный Ташкентский плов 🍚, сочные манты 🥟, свеп-свежая выпечка 🥐 будут радовать Вас каждый день!😋</p>

<p>У нас Вы сможете быстро взять еду🚀 и забрать её с собой🥡, при том, что она будет всегда свежая, только с огня 🔥, 
а если захотите полакомиться «здесь и сейчас» то уютный интерьер🪑 будет радовать Вас с 10-ти до 2-х ночи!🤪</p>

<p>Восточный стрит-фуд number ONE🔝</p>
<p>Сенбесең - попробуй САМ!😌</p>
"""


class Command(BaseCommand):
    help = 'Populate the database'

    @staticmethod
    def populate():
        models_helpers.Faqs(
            name="Можно ли заказать с разных заведений в одном заказе?",
            description="Да! Вы можете выбрать еду из разных ресторанов, положить в корзинку, оплатить заказ и ждать свой заказ!"
        ).save()

        models_helpers.Faqs(
            name="Я являюсь сотрудником компании, которая еще не зарегистрирована на вашем сайте, что мне делать?",
            description="Оставьте заявку, мы свяжемся с Вами в ближайшем времени и осуществим регистрацию!"
        ).save()

        models_helpers.Faqs(
            name="До какого периода времени я должен сделать заказ?",
            description="Обед - до 11:00, ужин - до 16:00"
        ).save()

        users = [
            User(username="user", first_name="Данил", last_name="Мельников", is_superuser=True, is_staff=True),
            User(username="almau", first_name="Алмаю", last_name="Университет"),
            User(username="one_technologies", first_name="One", last_name="Technologies"),
        ]

        for x in range(100):
            users.append(User(username=faker.user_name(), first_name=faker.first_name(), last_name=faker.last_name()))

        for user in users:
            user.set_password("1234")
            user.save()

        print("Users created successfully")

        # ---------------------
        addresses = [
            models_helpers.Location(name='МЕГА, Розыкабиева'),
            models_helpers.Location(name='Розабакиева 220'),
            models_helpers.Location(name='Мега вверхняя'),
        ]

        for x in range(20):
            addresses.append(models_helpers.Location(name=faker.address()))

        for address in addresses:
            address.save()

        print("Addresses created successfully")

        # ---------------------
        phones = []
        for x in range(20):
            phones.append(models_company.Phone(name=str(random.randint(10 ** 6, 10 ** 10))))

        for phone in phones:
            phone.save()

        print("Phone created successfully")

        companies = [
            # models_company.Company(name='Лагман Сити', user=users[6], role='restaurant',
            #                        description="Фаст-фуд Плов в коробочке. Восточная кухня. Средний чек 1200-1500тг.Т РЦ Mega Center ул. Розыбакие"),
            # models_company.Company(name='У Тимурчика', user=users[5], role='restaurant',
            #                        description="Блинчики с разными начинками, вкусные, хрустящие, с шоколадом"),
            # models_company.Company(name='Хлеб.kz', user=users[7], role='restaurant',
            #                        description="Домашний испеченный хлеб, натуральные ингрдиенты"),
            models_company.Company(name='АлмаЮ', user=users[1], role='company',
                                   description=""),
            models_company.Company(name='One Technologies', user=users[2], role='company',
                                   description=""),
        ]

        for company in companies:
            company.save()
            for _ in range(random.randint(1, 3)):
                company.phones.add(random.choice(phones))

        print("Restaurants created successfully")

        # ---------------------
        companies_addresses = []

        for x in range(20):
            companies_addresses.append(
                models_company.CompanyAddress(
                    name=faker.name(),
                    location=random.choice(addresses),
                    company=random.choice(companies),
                ),
            )

        for restaurant_address in companies_addresses:
            restaurant_address.save()
            for x in range(random.randint(1, 3)):
                restaurant_address.phones.add(random.choice(phones))

        print("Restaurant Addresses created successfully")
        # ---------------------
        categories = [
            # models_menu.Category(name='Национальное кухня'),
            # models_menu.Category(name='Европейская кухня'),
            # models_menu.Category(name='Китайская кухня'),
            # models_menu.Category(name='Суши'),
            # models_menu.Category(name='Fast Food'),
            # models_menu.Category(name='Продуктовые бренды'),
            # models_menu.Category(name='Пицца'),
            # models_menu.Category(name='Кухни мира'),
            # models_menu.Category(name='Кофейни'),
            # models_menu.Category(name='Десерты'),
            # models_menu.Category(name='Корейская кухня'),
        ]

        for category in categories:
            category.save()

        print("Categories Addresses created successfully")
        # ---------------------
        units = [
            models_menu.Units(name='грамм'),
            models_menu.Units(name='мл'),
            models_menu.Units(name='порция'),
            models_menu.Units(name='кг'),
            models_menu.Units(name='литр'),
            models_menu.Units(name='шт'),
        ]

        for unit in units:
            unit.save()

        print("Units created successfully")
        # ---------------------
        meals = []

        # for i in range(100):
        #     meals.append(models_menu.Meal(**meal_generation(units, companies_addresses)))
        #
        # for meal in meals:
        #     meal.save()
        # for x in range(random.randint(1, 5)):
        #     meal.categories.add(random.choice(categories))

        # for x in range(random.randint(1, 20)):
        #     models_menu.Comments(meal=meal, name=" ".join(faker.words(random.randint(5, 30))),
        #                          user=random.choice(users)).save()

    def read_csv(self):
        with open("populate/omnon.csv", encoding="windows-1251") as file:
            categories = {}
            units = {}

            user = User(username="omnon")
            user.set_password("1234")
            user.save()

            company = models_company.Company.objects.get_or_create(
                name='Om Nom',
                user=user,
                role='restaurant',
                description=description_rest,
                image="/company/cover/omnom.jpg"
            )[0]
            location = models_helpers.Location.objects.get_or_create(name="Сатпаева 30/1, Алматы, Казахстан")[0]
            address = models_company.CompanyAddress.objects.get_or_create(location=location, company=company)[0]

            for line in file.readlines()[1:]:
                name, size, unit, description, price, category, picture = line.strip().split(";")

                if category not in categories:
                    categories[category] = models_menu.Category.objects.get_or_create(name=category)[0]
                if unit not in units:
                    units[unit] = models_menu.Units.objects.get_or_create(name=unit)[0]

                category = categories[category]
                unit = units[unit]

                photo = models_menu.MealAlbum.objects.get_or_create(
                    user=user,
                    main=True,
                    photo=f"/menu/meals/omnon/{picture}"
                )[0]

                meal = models_menu.Meal.objects.get_or_create(
                    name=name,
                    address=address,
                    price=price,
                    description=description,
                    size=size,
                    units=unit,
                )[0]

                meal.categories.add(category)
                meal.album.add(photo)

    def handle(self, *args, **options):
        if User.objects.filter(username='user').exists():
            self.stdout.write('DB was populated before')
            return

        self.populate()

        self.read_csv()

        self.stdout.write(self.style.SUCCESS('Successfully populated'))


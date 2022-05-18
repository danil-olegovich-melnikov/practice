import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from helpers import models as models_helpers
from menu import models as models_menu
from company import models as models_company
from faker import Faker

faker = Faker("ru_RU")


def meal_generation(units, addresses):
    name = random.choice(food_names).capitalize()
    price = random.randint(2, 50) * 100
    description = " ".join(faker.words(random.randint(5, 50)))
    size = random.randint(1, 400)
    units = random.choice(units)
    address = random.choice(addresses)

    return {
        "name": name,
        "price": price,
        "description": description,
        "size": size,
        "units": units,
        "address": address,
    }


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
            models_company.Company(name='Лагман Сити', user=users[6], role='restaurant',
                                   description="Фаст-фуд Плов в коробочке. Восточная кухня. Средний чек 1200-1500тг.Т РЦ Mega Center ул. Розыбакие"),
            models_company.Company(name='У Тимурчика', user=users[5], role='restaurant',
                                   description="Блинчики с разными начинками, вкусные, хрустящие, с шоколадом"),
            models_company.Company(name='Хлеб.kz', user=users[7], role='restaurant',
                                   description="Домашний испеченный хлеб, натуральные ингрдиенты"),
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
                    restaurant=random.choice(companies),
                ),
            )

        for restaurant_address in companies_addresses:
            restaurant_address.save()
        for x in range(random.randint(1, 3)):
            restaurant_address.phones.add(random.choice(phones))

        print("Restaurant Addresses created successfully")
        # ---------------------
        categories = [
            models_menu.Category(name='Национальное кухня'),
            models_menu.Category(name='Европейская кухня'),
            models_menu.Category(name='Китайская кухня'),
            models_menu.Category(name='Суши'),
            models_menu.Category(name='Fast Food'),
            models_menu.Category(name='Продуктовые бренды'),
            models_menu.Category(name='Пицца'),
            models_menu.Category(name='Кухни мира'),
            models_menu.Category(name='Кофейни'),
            models_menu.Category(name='Десерты'),
            models_menu.Category(name='Корейская кухня'),
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

        for i in range(100):
            meals.append(models_menu.Meal(**meal_generation(units, companies_addresses)))

        for meal in meals:
            meal.save()
        for x in range(random.randint(1, 5)):
            meal.categories.add(random.choice(categories))

        for x in range(random.randint(1, 20)):
            models_menu.Comments(meal=meal, name=" ".join(faker.words(random.randint(5, 30))),
                                 user=random.choice(users)).save()

        print("Meals created successfully")

    def handle(self, *args, **options):
        if User.objects.filter(username='user').exists():
            self.stdout.write('DB was populated before')
            return

        self.populate()

        self.stdout.write(self.style.SUCCESS('Successfully populated'))


food_names = """
abiyuch
acerola
acorn
agave
agents
agutuk
alfalfa
amaranth
animal
apache
apple
apples
applesauce
apricot
apricots
arrowhead
arrowroot
artichokes
artificial
arugula
ascidians
asparagus
avocados
baby
babyfood
bacon
bagel
bagels
baking
balls
balsam-pear
bamboo
bananas
bar
barbecue
barley
bars
basil
bean
beans
bear
beef
beerwurst
beet
beets
berry
besan
beverage
beverages
biscuits
bison
bits
bitter
blackberries
blackberry
blackeyes
blend
blueberries
blueberry
bockwurst
bologna
borage
bowl
boysenberries
bran
brand
bratwurst
braunschweiger
bread
breadfruit
breakfast
breast
broadbeans
broccoli
broth
brotwurst
brussels
buckwheat
buffalo
bulgur
buns
burdock
burgers
burrito
butter
butterbur
butters
cabbage
cake
candied
candies
capers
carambola
carbonated
cardoon
caribou
carissa
carne
carob
carob-flavor
carrot
carrots
cassava
catsup
cattail
cauliflower
celeriac
celery
celtuce
cereal
cereals
chard
chayote
cheese
cheesecake
cheesefurter
cherimoya
cherries
chewing
chicken
chickpea
chickpeas
chicory
chilchen
child
chili
chips
chiton
chives
chocolate
chocolate-flavor
chocolate-flavored
chokecherries
chorizo
chrysanthemum
cilantro
cinnamon
citronella
citrus
clam
clementines
cloudberries
cockles
cocktail
cocoa
coffee
coffeecake
collards
commercially
concentrate
cone
cones
confectionery
containing
cookie
cookies
coriander
corn
corned
cornmeal
cornsalad
cornstarch
cotija
couscous
cowpeas
crabapples
cracker
crackers
cranberries
cranberry
cranberry-apple
cranberry-apricot
cranberry-grape
cranberry-orange
cream
creams
creamy
cress
croissants
croutons
crumbs
crust
crustaceans
cucumber
currants
custard-apple
custards
dairy
dandelion
danish
dates
deer
dessert
desserts
diabetes
dill
dinner
dip
dishes
dock
dogs
dough
doughnuts
dove
dressing
drink
drippings
drumstick
dry
duck
dulce
durian
dutch
ear
edamame
egg
eggnog
eggnog-flavor
eggplant
eggs
elderberries
elk
emu
endive
energy
entrees
epazote
eppaw
extender
extract
falafel
fast
fat
fava
feijoa
fennel
fern
ferns
fiddlehead
figs
fillets
fillings
fireweed
fish
flakes
flan
flavored
flour
flours
flower
flowers
fluid
focaccia
foie
food
foods
formula
formulated
frankfurter
franks
frijoles
frog
from
frostings
frozen
fruit
fruit-flavored
frybread
frying
fungi
garbanzo
garlic
gelatin
gelatins
germ
ginger
gluten
goat
goose
gooseberries
gourd
grain
gram
granola
grape
grapefruit
grapes
gras
grass
gravy
green
greens
groats
ground
groundcherries
grouse
guacamole
guanabana
guava
guavas
guinea
gum
gums
ham
hazelnut
hazelnuts
headcheese
hearts
hen
hibiscus
hips
hominy
honey
horned
horseradish
household
huckleberries
hummus
hush
hyacinth
hyacinth-beans
hydrogenated
hydrolyzed
ice
imitation
incaparina
industrial
isolate
jackfruit
jams
java-plum
jellies
jellyfish
jerusalem-artichokes
jicama
juice
jujube
jute
kale
kanpyo
keikitos
kielbasa
kiwano
kiwifruit
knackwurst
kohlrabi
kumquats
lamb
lambs
lambsquarters
lard
lasagna
lean
leavening
leaves
lebanon
leche
leeks
legs
lemon
lemonade
lemonade-flavor
lemons
lentils
lettuce
lima
lime
limeade
limes
link
links
lion
litchis
liver
liverwurst
loaf
loganberries
loin
longans
loquats
lotus
lulo
lunch
luncheon
lupins
luxury
macaroni
made
malabar
malt
malted
mammy-apple
mango
mangos
mangosteen
maraschino
margarine
margarine-like
marmalade
mashu
mayonnaise
meal
meat
meatballs
meatloaf
melon
melons
milk
millet
miso
mixed
mocha
molasses
mollusks
moose
mortadella
mothbeans
mother's
mountain
mouse
muffin
muffins
mulberries
mung
mungo
mush
mushrooms
mustard
mutton
nance
naranjilla
natto
navajo
nectar
nectarines
nettles
new
noodles
nopales
novelties
nutritional
nuts
oat
oats
octopus
oheloberries
oil
oil-butter
okara
okra
olive
olives
onion
onions
oopah
orange
orange-flavor
orange-grapefruit
oranges
ostrich
oven-roasted
palm
pancakes
papad
papaya
papayas
parfait
parmesan
parsley
parsnips
passion-fruit
pasta
pastrami
pastries
pastry
pate
patties
patty
pea
peach
peaches
peanut
peanuts
pear
pears
peas
pectin
peel
people
pepeao
pepper
peppered
peppermint
pepperoni
peppers
persimmons
pheasant
phyllo
pickle
pickles
picnic
pie
pigeon
pigeonpeas
piki
pimento
pimiento
pineapple
pinon
pitanga
pizza
plain
plantains
plums
pockets
pokeberry
pomegranate
pomegranates
popcorn
pork
potato
potatoes
potsticker
poultry
powder
prairie
prepared
preserves
pretzels
prickly
product
products
protein
prune
prunes
pudding
puddings
puff
puffs
pulled
pulp
pummelo
pumpkin
punch
punch-flavor
puppies
puree
purslane
quail
quarters
queso
quinces
quinoa
raab
radicchio
radish
radishes
raisins
rambutan
raspberries
ravioli
ready-to-drink
ready-to-eat
red
reddi
reduced
refried
relish
rennin
replacement
restaurant
rhubarb
rice
rings
roast
rojos
roll
rolls
root
roots
rose
rose-apples
roselle
rosemary
rowal
ruffed
rutabagas
rye
salad
salami
salmon
salmonberries
salsify
salt
sandwich
sapodilla
sapote
sauce
sauerkraut
sausage
school
scrapple
sea
seal
seasoning
seaweed
seeds
semolina
sesbania
shake
shakes
shallots
shell
shells
sherbet
shoots
shortening
shoyu
side
smelt
smoked
smoothie
snack
snacks
sorghum
souffle
soup
sourdock
soursop
soy
soybean
soybeans
soyburgers
soymilk
spaghetti
spanish
spearmint
spelt
spices
spinach
split
spread
sprouts
squab
squash
squirrel
steelhead
stew
stew/soup
sticks
stinging
strawberries
strawberry-flavor
strudel
stuffing
substitute
substitutes
succotash
sugar
sugar-apples
sugars
supplement
swamp
sweet
sweetener
sweeteners
swisswurst
syrup
syrups
taco
tamales
tamari
tamarind
tamarinds
tangerine
tangerines
tannier
tapioca
taquitos
taro
tart
tea
teff
tempeh
tenders
tennis
thigh
thuringer
thyme
toast
toaster
toddler
tofu
tomatillos
tomato
tomatoes
topping
toppings
tortellini
tortilla
tortillas
tostada
triticale
trout
tuber
tunicate
tunughnak
turkey
turnip
turnips
turnover
turtle
twists
vanilla
veal
vegetable
vegetable-oil
vegetables
vegetarian
veggie
venison
vermicelli
vinegar
vinespinach
vital
volteados
waffle
waffles
walrus
wasabi
water
waterchestnuts
watercress
watermelon
waxgourd
weed
wheat
whey
whiskey
whole
wild
willow
wine
winged
wocas
wonton
wrappers
yachtwurst
yam
yambean
yardlong
yautia
yeast
yellow
yogurt
yogurts
zealand
zwieback
"""

food_names = food_names.strip().split()

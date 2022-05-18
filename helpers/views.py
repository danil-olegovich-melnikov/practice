from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from company.models import Company, CompanyAddress
from helpers.models import Form, Faqs
from menu.models import Meal, Category, Order
from django.http import HttpResponseNotFound


# Create your views here.
def homepage(request):
    return render(request, 'helpers/index.html')


def search(request):
    data = {}
    meals = Meal.objects.all()
    categories = Category.objects.all()
    page_number = 1

    try:
        user_company = Company.objects.get(user=request.user)
        addresses = CompanyAddress.objects.filter(company=user_company)
    except:
        user_company = ""
        addresses = ""

    if request.method == "POST":
        food_name = request.POST.get("food_name", "")
        page_number = request.POST.get("page_number", 1)
        if not str(page_number).isdigit():
            page_number = 1

        pks = []
        for key in request.POST:
            if key.startswith("category"):
                pk = key.replace("category-", "")
                pks.append(int(pk))

        if len(pks) > 0:
            meals = meals.filter(categories__in=pks)

        if food_name != "":
            meals = meals.filter(name__icontains=food_name)
            data['food_name'] = food_name

    if request.method == "GET":
        address = request.GET.get('address', "")
        company = request.GET.get('company', "")

        if len(address) > 0:
            meals = meals.filter(address_id=address)
        elif len(company) > 0:
            meals = meals.filter(address_id__in=CompanyAddress.objects.filter(restaurant_id=company))

    meals = Paginator(meals, 9)
    data['meals'] = meals.page(page_number)
    data['pages'] = meals.page_range
    data['page_number'] = page_number
    data['categories'] = categories
    data['user_addresses'] = addresses

    return render(request, 'helpers/search.html', data)


def form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        type = request.POST.get("type", "")
        contact = request.POST.get("contact", "")
        description = request.POST.get("description", "")

        try:
            Form(name=name, type=type, contact=contact, description=description).save()
        except:
            pass

    return redirect('/')


def restaurants(request):
    companies = Company.objects.filter(role='restaurant')
    return render(request, "helpers/restaurants.html", {"companies": companies})


def faqs(request):
    faqs = Faqs.objects.all()
    return render(request, 'helpers/faqs.html', {"faqs": faqs})


def restaurant(request, pk):
    try:
        company = Company.objects.get(id=pk, role='restaurant')
        company_addresses = CompanyAddress.objects.filter(company=company)

        data = {
            "company": company,
            "company_addresses": company_addresses,
        }

        return render(request, "helpers/restaurant.html", data)
    except:
        return redirect("/")


def process_order(request):
    if request.method == "POST":
        order = Order.objects.create(
            delivery_date=request.POST.get("delivery_date", ""),
            time_delivery=request.POST.get("time_delivery", ""),
            name=request.POST.get("name", ""),
            phone=request.POST.get("phone", ""),
            address=request.POST.get("address", ""),
            description=request.POST.get("description", ""),
        )

        meals = str(request.POST.get("meals")),
        user = request.user

        if user.is_authenticated:
            try:
                company_address = int(request.POST.get("company_address"))
                company = Company.objects.get(user=user)
                address = CompanyAddress.objects.get(company=company, id=company_address)
                order.user = address
                order.save()
            except:
                pass

        amount = 0
        for pair in meals[0].split("|"):
            pk = pair.split("-")
            if pk[0].strip():
                meal = Meal.objects.get(pk=int(pk[0]))
                order.meals.add(meal)
                amount += meal.price

        order.amount = amount
        order.save()

        return redirect("/success_order/")

def success_order(request):
    return render(request, "helpers/success-order.html")

def view_orders(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return HttpResponseNotFound()

    data = {
        "orders": Order.objects.all(),
    }

    return render(request, "helpers/all_orders.html", data)
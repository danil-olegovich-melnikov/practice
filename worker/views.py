from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def register(request: HttpRequest) -> HttpResponse:
    context = {"message": "", "username": "", "email": "", "user": request.user}
    if request.method == "POST":
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        error = ""
        if username == "":
            error = "Введите имя пользователя"
        elif email == "" or "@" not in email:
            error = "Введите свою почту"
        elif password1 == "":
            error = "Введите пароль"
        elif password1 != password2:
            error = "Пароли не совпадают"
        elif User.objects.filter(username=username).count() > 0:
            error = "Данный никнейм уже занят"

        if error == "":
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect("/")

        context["username"] = username
        context["email"] = email
        context["message"] = error

    return render(request, "registration/register.html", context=context)

from django.urls import path
from helpers import views

app_name = 'helpers'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='search'),
    path('form/', views.form, name='form'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('restaurants/<int:pk>', views.restaurant, name='restaurant'),
]

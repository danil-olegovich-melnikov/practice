from django.urls import path
from helpers import views

app_name = 'helpers'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='search'),
]

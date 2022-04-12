from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include("restaurant.urls")),
    path('menu/', include("menu.urls")),
]

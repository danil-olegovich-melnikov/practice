from django.urls import path, reverse
import django.contrib.auth.views as auth_views
from worker.views import register

app_name = 'worker'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),
    path('reqister/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/auth/login/'), name='logout'),
]

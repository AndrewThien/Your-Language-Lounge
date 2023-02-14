from django.urls import path, include
from . import views

app_name = 'user_register'
urlpatterns = [
    path('', views.user_register, name='user_register'),
    path('success/', views.register_success, name='register_success'),
]
from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('logout_mess/', views.logout_user_mess, name='logout_user_mess'),
]
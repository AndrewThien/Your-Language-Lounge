from django.urls import path, include
from . import views

app_name = 'why_us'
urlpatterns = [
    path('our_values', views.our_values, name='our_values'),
    path('our_teachers', views.our_teachers, name='our_teachers'),
]
from django.urls import path, include
from . import views

app_name = 'classes'
urlpatterns = [
    path('communicative/', views.communicative, name='communicative'),
    path('ielts/', views.ielts, name='ielts'),
]
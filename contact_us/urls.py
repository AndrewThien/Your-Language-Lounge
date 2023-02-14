from django.urls import path, include
from . import views
from .views import contactView, successView

app_name = 'contact_us'
urlpatterns = [
    path("contact/", contactView, name="contact_us"),
    path("success/", successView, name="success"),
]
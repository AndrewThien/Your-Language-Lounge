"""YourLanguageLounge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('classes/', include('classes.urls')),
    path('why_us/', include('why_us.urls')),
    path('your_library/', include('your_library.urls')),
    path('user_auth/', include('user_auth.urls')),
    path('user_register/', include('user_register.urls')),
    path('contact_us/', include('contact_us.urls')),
]

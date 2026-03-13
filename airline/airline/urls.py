"""
URL configuration for airline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from flights.views import home, search_flights
from django.urls import include

urlpatterns = [
    path("", home,name="home"),
    path('flights/', include("flights.urls")),
    path('users/', include("users.urls")),
    path('admin/', admin.site.urls),
    path("search/", search_flights, name="search_flights"),
]

"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    # api
    path('api/create_csv/', views.CreateCsv.as_view(), name="create_csv"),
    path('api/read_csv/', views.ReadCsv.as_view(), name="read_csv"),
    path('api/calculation/', views.Calculation.as_view(), name="calculation"),
]

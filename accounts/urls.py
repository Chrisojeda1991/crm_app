from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse


urlpatterns = [
    path('',views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]
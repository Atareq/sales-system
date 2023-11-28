from django.contrib import admin
from django.urls import path
from .API import ProductAPI

urlpatterns = [
    path('product/', ProductAPI.as_view()),
]
from django.contrib import admin
from django.urls import path
from .API import TraderReceiptAPI

urlpatterns = [
    path('receipt/', TraderReceiptAPI.as_view()),
    # i must make unigue url bet trader abd customer
]
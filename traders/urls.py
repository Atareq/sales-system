from django.contrib import admin
from django.urls import path
from cashier_shift.views import *

urlpatterns = [
    path('traders/', admin.site.urls),
]
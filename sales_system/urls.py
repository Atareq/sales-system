from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls') ),
    # path('cashier_shift/', include('cashier_shift.urls')),
    # path('employee/', include('employe.urls')),
    path('', include('product.urls')),
    path('', include('receipt.urls')),
    # path('sales_system/', include('sales_system.urls')),
    # path('traders/', include('traders.urls')),
]


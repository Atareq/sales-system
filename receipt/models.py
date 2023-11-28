from django.db import models
from django.utils import timezone
from user.models import CustomUser
from traders.models import Trader
class TraderReceipt (models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    kinds_number = models.IntegerField(default=0,null= True)
    time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    piad = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    rest_of_money = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # "rest_of_money"can be in minus if it in buying condition and will be added 
    # to the debut in trader table 
    trader = models.ForeignKey(Trader, on_delete=models.SET_NULL, null=True)

class CustomerReceipt (models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    kinds_number = models.IntegerField(default=0,null= True)
    profit = models.DecimalField(max_digits=10, decimal_places=2,default=0)    
    time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    piad = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    rest_of_money = models.DecimalField(max_digits=10, decimal_places=2,default=0)
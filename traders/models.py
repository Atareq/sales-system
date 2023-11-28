from django.db import models

class Trader(models.Model):

    trader = models.CharField(max_length=40)
    address = models.CharField(max_length=60)
    debut = models.DecimalField(max_digits=10, decimal_places=2)

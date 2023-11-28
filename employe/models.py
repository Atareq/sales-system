from django.db import models
from user.models import CustomUser

class Employe(models.Model):
    # when admin add a new employe we will write its 
    # username and i will save it as a forigen key here
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)
    # sometimes te employe will not have a username
    name = models.CharField(max_length=50)
    job_title =  models.CharField(max_length=40)
    national_id = models.CharField(max_length=14)
    phone_num = models.CharField(max_length=11)
    address =  models.CharField(max_length=80)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    subtract = models.DecimalField(max_digits=10, decimal_places=2)
    #h3ml table tani l fatowrt al 5somat kol shahr
from django.db import models
from datetime import datetime, timedelta
from user.models import CustomUser

class cashier_shift(models.Model):

    user_fk = models.ForeignKey(CustomUser,on_delete= models.DO_NOTHING)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_payments = models.DecimalField(max_digits=10, decimal_places=2)
    money_required = models.DecimalField(max_digits=10, decimal_places=2)
    # start_shift  = models.DateTimeField() becase there is 'last_login' feild in the user model
    end_shift = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        
        my_id = self .id
        last_id = cashier_shift.objects.get(id =my_id - 1 )
        self.start_shift = datetime.now()
        
        super().save(*args, **kwargs)

  
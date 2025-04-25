from django.db import models
from Customer.models import Customer
# Create your models here.

class Payment(models.Model):
        customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
        paid_amount = models.DecimalField(max_digits=10,decimal_places=2)
        discount = models.DecimalField(max_digits=10,decimal_places=2)
        tot_amount = models.DecimalField(max_digits=10,decimal_places=2)
        payment_date = models.DateTimeField()


        class Meta:
                db_table='Payments'
        



from django.db import models
from Customer.models import Customer

# Create your models here.
class Loan(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    #item_name = models.ForeignKey

    class Meta:
        db_table='Loans'
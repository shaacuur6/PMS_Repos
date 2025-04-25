from django.db import models
from Stock.models import Stock
from django.contrib.auth.models import User
from Branches.models import Branch
# Create your models here.

trans_choice=(('Cash','Cash'),('Credit','Credit'))
class Sale(models.Model):
    item_name =  models.ForeignKey(Stock,on_delete=models.CASCADE)
    item_qty = models.IntegerField()
    item_price = models.DecimalField(max_digits=10,decimal_places=2)
    sales_date = models.DateField()
    uname = models.ForeignKey(User,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    trans_type = models.CharField(max_length=6,choices=trans_choice)

    class Meta:
        db_table='Sales'
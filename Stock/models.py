from django.db import models
from Items.models import Item
from Branches.models import Branch
from django.contrib.auth.models import User
from Supplier.models import Supplier
# Create your models here.

mode_names=(('Cash','Cash'),('Credit','Credit'))
class Stock(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    trans_mode = models.CharField(max_length=6,choices=mode_names,default='Cash')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,default=1)
    item_qty = models.IntegerField()
    item_price = models.DecimalField(max_digits=10,decimal_places=2)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    uname = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.item}"
    
    class Meta:
        db_table='Stocks'

    


    
from django.db import models
from Category.models import Item_Category

# Create your models here.
measure_options=(('Pcs','Pcs'),('Box','Box'))
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    measurement_name = models.CharField(max_length=3,choices=measure_options,default='Pcs')
    category = models.ForeignKey(Item_Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.item_name
    
    
    class Meta:
        db_table='Items'


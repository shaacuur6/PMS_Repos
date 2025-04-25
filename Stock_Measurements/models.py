from django.db import models
from Items.models import Item
# Create your models here.
class Measurement(models.Model):
    measurement_name = models.ForeignKey(Item,on_delete=models.CASCADE)

    class Meta:
        db_table='Measurements'
    

    
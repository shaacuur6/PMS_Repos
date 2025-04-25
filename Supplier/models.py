from django.db import models
from django.contrib.auth.models import User

# Create your models here.
gender_choice=(('M','Male'),('F','Female'))
class Supplier(models.Model):
    Name = models.CharField(max_length=100)
    Tel = models.IntegerField(null=True,blank=True)
    Gender = models.CharField(max_length=1,choices=gender_choice)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Reg_Date = models.DateField(null=True)
    Created_By = models.ForeignKey(User,on_delete = models.CASCADE,related_name='Supp_Created_By',default=1)
    Updated_By = models.ForeignKey(User,on_delete = models.CASCADE,related_name='Supp_Updated_By',default=1)
    Updated_At = models.DateTimeField(null=True)

    def __str__(self):
        return self.Name

    class Meta:
        db_table='Suppliers'



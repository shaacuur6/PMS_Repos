from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name
    
    class Meta:
        db_table='Branch'
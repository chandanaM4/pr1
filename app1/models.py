from  django.db import models

class student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20) 
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()

 
# Create your models here.

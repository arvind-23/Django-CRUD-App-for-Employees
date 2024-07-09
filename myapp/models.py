from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    empid=models.IntegerField()
    email=models.EmailField(blank=True)
    role=models.CharField(max_length=50)
    salary=models.FloatField()
    picture=models.ImageField()


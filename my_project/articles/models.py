from django.db import models

# Create your models here.

class Patient(models.Model):
    UName=models.CharField(max_length=100)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=1)
    Phone=models.IntegerField()
    EmailID=models.EmailField(max_length=254)
    StreetAdress=models.TextField()
    city=models.TextField()
    PostalCode=models.TextField()

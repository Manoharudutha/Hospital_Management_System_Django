from pyexpat import model
from tokenize import Special
from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Special=models.CharField(max_length=50)

class Patient(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=1)
    Mobile=models.IntegerField()
    Address=models.TextField()
 
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()

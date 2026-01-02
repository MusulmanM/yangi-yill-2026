from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Direktor(models.Model):
    pass 





class Oquvchi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=False)
    kurs = models.IntegerField(blank=True, null=False)
    raqam = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    


    
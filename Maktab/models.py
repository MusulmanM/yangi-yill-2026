from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Maktab(models.Model):
    name = models.CharField(max_length=150)
    manzil = models.CharField(max_length=250)
    soni = models.IntegerField(blank=True, null=True)
    maktab_ochilgan = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)





# Direktor class forinkey user, oylik, ishga-kelgan-vaqt, yaratilgan vaqt
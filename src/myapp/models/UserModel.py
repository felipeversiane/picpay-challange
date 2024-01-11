from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from myapp.validators import *

TYPE_CHOICES = (
        ['M',"Merchant"],
        ['C',"Common"],       
)

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255,verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    document = models.CharField(max_length=14, unique=True, verbose_name="Document")
    email = models.EmailField(unique=True, verbose_name="Email")
    balance = models.DecimalField(verbose_name="Balance")
    user_type = models.CharField(max_length=1,choices=TYPE_CHOICES,default="C",null=False,blank=False, verbose_name="User Type")

    def __str__(self):
        return "{}-{}-{}".format(self.first_name,self.last_name,self.balance)
    
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ['id']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
    


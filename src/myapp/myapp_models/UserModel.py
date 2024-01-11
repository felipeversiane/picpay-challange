# from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from myapp.validators import *

TYPE_CHOICES = (
        ['M',"Merchant"],
        ['C',"Common"],       
)

# You can use AbstractUser to extend the Django User
class CustomUser(models.Model):
    first_name = models.CharField(max_length=255,null=False,blank=False,verbose_name="First Name",validators=[validate_letters,validate_first_letter])
    last_name = models.CharField(max_length=255,null=False,blank=False, verbose_name="Last Name",validators=[validate_letters,validate_first_letter])
    document = models.CharField(max_length=14, unique=True, verbose_name="Document")
    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.CharField(max_length=255,null=True,blank=True) # In this case we don't need to use this password
    balance = models.DecimalField(verbose_name="Balance",max_digits=10, decimal_places=2,null=False,blank=False,default=0)
    user_type = models.CharField(max_length=1,choices=TYPE_CHOICES,default="C",null=False,blank=False, verbose_name="User Type",validators=[validate_first_letter])

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
    


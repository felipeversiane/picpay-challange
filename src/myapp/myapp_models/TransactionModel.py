from django.db import models
from rest_framework import serializers
from .UserModel import CustomUser
from myapp.validators import *
from myapp.managers import  TransactionManager 

class Transaction(models.Model):
    amount = models.DecimalField(verbose_name="Transaction Amount",max_digits=10, decimal_places=2,null=False,blank=False,validators=[validate_value])

    payer = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING, null=False, blank=False, 
                              verbose_name="Transaction Payer",related_name='payer_transactions')
    
    payee = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING, null=False, blank=False, 
                              verbose_name="Transaction Payee",related_name='payee_transactions')
    
    transaction_date = models.DateTimeField(auto_now_add=True, verbose_name="Date and Time",validators=[validate_date,validate_time])

    objects = TransactionManager()
    
    def __str__(self):
        return "{}-{}-{}-{}".format(self.payer.username, self.payee.username, self.amount, self.transaction_date.strftime('%d-%m-%Y %H:%M'))

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['id']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionCreateSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=10, decimal_places=2,validators=[validate_value])
    payer = serializers.IntegerField()
    payee = serializers.IntegerField()
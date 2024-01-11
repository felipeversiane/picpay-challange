from django.db import models
from rest_framework import serializers
from .UserModel import CustomUser
from myapp.validators import *
from myapp.managers import TransactionManager 

class Transaction(models.Model):
    amount = models.DecimalField(verbose_name="Transaction Amount")
    payer = models.ForeignKey(CustomUser, null=False, blank=False, verbose_name="Transaction Payer")
    payee = models.ForeignKey(CustomUser, null=False, blank=False, verbose_name="Transaction Payee")
    transaction_date = models.DateTimeField(auto_now_add=True, verbose_name="Date and Time")

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

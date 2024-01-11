import requests
from django.db import models
from myapp.myapp_models.UserModel import CustomUser
from django.core.exceptions import ValidationError
from .validators import *

class TransactionManager(models.Manager):
    
    def create_transaction(self, transaction_data):
        payer_id = transaction_data.get("payer")
        payee_id = transaction_data.get("payee")
        amount = transaction_data.get("value")

        payer = CustomUser.objects.get(id=payer_id)
        payee = CustomUser.objects.get(id=payee_id)

        validate_transaction(payer, amount)

        if self.authorize_transaction(payer, amount):
            transaction = self.create( 
                amount=amount,
                payer=payer,
                payee=payee
            )
            payer.balance -= amount
            payee.balance += amount

            payer.save()
            payee.save()

            return transaction

        else:
            raise ValidationError("Transaction failed.")


    def authorize_transaction(self,payer, amount):
        API_URL = "https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc"

        try:
            response = requests.get(API_URL)
            response.raise_for_status()  
            response_data = response.json()

            if response_data.get("result") != "ok" and response_data.get("message") != "Autorizado":
                return False
            return True

        except requests.RequestException as e:
            raise ValidationError(f"Network Error: {e}")

        except ValueError as e:
            raise ValidationError(f"Json Error: {e}")


    def send_notification(payee,message):
           email = payee.email  
           API_URL = 'https://run.mocky.io/v3/54dc2cf1-3add-45b5-b5a9-6bf7e7f1f4a6'
           response = requests.get(API_URL)
           response.raise_for_status()  
           response_data = response.json()
           if response_data.get("result") != "ok" :
                 raise ValidationError("Email service is out.")
       
 
            
                        
           

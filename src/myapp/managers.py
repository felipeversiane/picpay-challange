import requests
from django.db import models
from myapp.models.UserModel import CustomUser
from myapp.validators import ValidationError
from validators import *

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

    @staticmethod
    def authorize_transaction(payer, amount):
        API_URL = "https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc"

        try:
            response = requests.get(API_URL)
            response.raise_for_status()  
            response_data = response.json()

            if response_data.get("result") == "ok" and response_data.get("message") == "Autorizado":
                return True
            else:
                return False

        except requests.RequestException as e:
            print(f"Network error: {e}")
            return False

        except ValueError as e:
            print(f"JSON Error: {e}")
            return False

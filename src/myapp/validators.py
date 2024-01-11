import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
import re


def validate_first_letter(str):    
    if str[0].isdigit():        
        raise ValidationError("First letter cannot be a number.")

def validate_letters(name):    
    if not re.match(r'^[A-Za-z ]+$', name):      
        raise ValidationError("Only letters and spaces allowed.")

def validate_value(value):
    if value <= 0:
        raise ValidationError("Value must be positive.")
        
def validate_date(date): 
    if date < timezone.now().date():  
        raise ValidationError("Invalid date.")
        
def validate_time(time):       
    if time < timezone.now().time():   
        raise ValidationError("Invalid time.") 
    
def validate_transaction(user,amount):
    if user.balance < amount:
        raise ValidationError("Balance lower than necessary.")
    if user.user_type == 'M':
        raise ValidationError("Merchant cannot make payments")

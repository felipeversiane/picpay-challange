from rest_framework import viewsets
from myapp.models.TransactionModel import *
from myapp.models.UserModel import *
from .permissions import *


'''

Generic viewsets

'''

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


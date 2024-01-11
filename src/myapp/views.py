from rest_framework import viewsets
from myapp.myapp_models.TransactionModel import *
from myapp.myapp_models.UserModel import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status


'''

Transaction View Set

'''

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = TransactionCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                transaction = Transaction.objects.create_transaction(serializer.validated_data)
                serialized_transaction = TransactionSerializer(transaction)
                return Response(serialized_transaction.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''

User View Set

'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


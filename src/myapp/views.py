from rest_framework import viewsets
from myapp.myapp_models.TransactionModel import *
from myapp.myapp_models.UserModel import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



'''

Transaction View Set

'''
@permission_classes([IsAuthenticated,IsPayer])
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = TransactionCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                transaction = Transaction.objects.create_transaction(serializer.validated_data, request.user)
                serialized_transaction = TransactionSerializer(transaction)
                return Response(serialized_transaction.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''

User View Set

'''

class UserViewSet(viewsets.ViewSet):
    serializer_class = CustomUserSerializer
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            if username is None:
                return Response({'message': 'Please provide a valid username.'}, status=status.HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(username=username).exists():
                return Response({'message': 'This username is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
            if not re.match(PASSWORD_REGEX, password):
                return Response({'message': 'Password does not meet the requirements.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'Successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



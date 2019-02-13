import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

class TransactionList(APIView):
    """
    Get a List of all Transactions from an account
    """
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = Account.objects.get(uuid=uuid_str)
        transactions = account.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, uuid):
        uuid_str = str(uuid)
        account = Account.objects.get(uuid=uuid_str)
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            if account.check_if_overdrawn(float(serializer.validated_data['amount'])):
                return HttpResponse("Insufficient Account balance")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AccountDetail(APIView):
    """
    Get details of one account by uuid
    """
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = Account.objects.get(uuid=uuid_str)
        #checks the balance of the account and save it to the db
        account.check_balance()
        account.save()
        serializer = AccountSerializer(account)
        return Response(serializer.data)

class AccountBalanceDetails(APIView):
    
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = Account.objects.get(uuid=uuid_str)
        #checks the balance of the account and save it to the db
        account.check_balance()
        account.save()
        serializer = AccountSerializer(account)
        return Response(serializer.data['balance'])
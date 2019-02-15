import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

class TransactionList(APIView):
    """
    GET api/account/uuid/transactions
    Get a List of all Transactions from an account
    """
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = get_object_or_404(Account, uuid=uuid_str)
        transactions = account.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, uuid):
        """
        POST api/account/uuid/transactions
        Creates a new transaction
        tests if the transaction makes the account balance go negative
        """
        uuid_str = str(uuid)
        account = get_object_or_404(Account, uuid=uuid_str)
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            if account.check_if_overdrawn(float(serializer.validated_data['amount'])):
                return HttpResponse("Insufficient Account balance, transaction will not be processed")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AccountDetail(APIView):
    """
    GET api/account/uuid
    Get the account details of one account
    """
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = get_object_or_404(Account, uuid=uuid_str)
        #checks the balance of the account and save it to the db
        account.check_balance()
        account.save()
        serializer = AccountSerializer(account)
        return Response(serializer.data)

#todo create a post request to create new account

class AccountBalanceDetails(APIView):
    """
    GET api/account/uuid/balance
    Get the balance for one account
    """
    
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = get_object_or_404(Account, uuid=uuid_str)
        #checks the balance of the account and save it to the db
        account.check_balance()
        account.save()
        serializer = AccountSerializer(account)
        return Response(serializer.data['balance'])
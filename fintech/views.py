from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Account, Transaction
from django.contrib.auth.models import User
from .serializers import AccountSerializer, TransactionSerializer

class TransactionList(APIView):
    """
    get:
    get a List of all Transactions from an account

    post:
    Creates a new transaction.
    Tests if the transaction makes the account balance go negative.
    """
    def get(self, request, uuid):
        uuid_str = str(uuid)
        account = get_object_or_404(Account, uuid=uuid_str)
        transactions = account.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, uuid):
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
    get:
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

class AccountBalanceDetails(APIView):
    """
    get:
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

class AccountList(APIView):
    """
    get:
    Get a list of all the accounts for a user specified by the user
    pk number

    post:
    Creates a new account for the user specified by the pk number
    """
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        accounts = Account.objects.filter(user=pk)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
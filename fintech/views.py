from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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

class AccountDetail(APIView):
    """
    Get details of one account
    """
    pass

class AccountBalanceDetails(APIView):
    pass
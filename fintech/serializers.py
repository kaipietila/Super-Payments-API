from .models import Account, Transaction
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('uuid', 'name', 'balance', 'user')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('uuid', 'account', 'transaction_date', 'amount',
                'description', 'active', 'create_time', 'update_time')


from .models import Account, Transaction
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('uuid', 'name', 'balance', 'user',)
        #fields that are read only and auto added when creating object
        read_only_fields = ('uuid',)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('uuid', 'account', 'transaction_date', 'amount',
                'description', 'active', 'create_time', 'update_time',)
        #fields that are read only and auto added when creating object
        read_only_fields = ('uuid', 'create_time', 'update_time',)

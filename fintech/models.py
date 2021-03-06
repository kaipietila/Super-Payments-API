from django.db import models
import uuid


class Account(models.Model):
    """
    Represents a bank account in the system.
    Balance is updated with the check_balance func
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default = 0.00)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    def check_balance(self):
        """
        Updating the account balance to the current sum of transactions.
        Returns the current balance.
        """
        self.balance = sum(
           t.amount for t in self.transactions.all() if t.active
        )
        return self.balance
    
    def check_if_overdrawn(self, transaction_amount):
        """
        Checks if a transaction overdraws the account. 
        Is done before each transaction is processed to ensure
        that account balance is not overdrawn.
        """
        current_balance = self.check_balance()
        #converting to float to be able to do the comparisons 
        if float(current_balance) + transaction_amount < 0:
            return True

class Transaction(models.Model):
    """
    Records transactions on account. You can think of these as entries
    on account statement.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(
        Account, related_name='transactions',
        on_delete=models.PROTECT)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=25, blank=True, default='')

    # If active is False, the transaction should not be visible to the
    # customer in any way.
    active = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
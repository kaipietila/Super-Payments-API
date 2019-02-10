from django.test import TestCase
from fintech.models import Account, Transaction
from django.contrib.auth.models import User
import datetime

class AccountTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testUser', password = 'testuser')
        self.account = Account.objects.create(name='testAccount', 
                                                balance=0.00, user=self.user)
        self.balanced_transaction = Transaction.objects.create(account=self.account, amount=50.00,
                                                            description='test', active=True,
                                                            transaction_date = datetime.datetime.now())
        self.account.check_balance()

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testUser')

    def test_account_creation(self):
        
        self.assertEqual(self.account.name, 'testAccount')
        self.assertEqual(self.account.balance, 50.00)
        self.assertEqual(self.account.user, self.user)
        self.assertTrue(self.account.uuid)

    def test_str_method(self):
        self.assertEqual(str(self.account), self.account.name)
    
    def test_account_balance_check(self):
        self.assertTrue(self.account.check_balance())

class AccountBalanceFailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testUser', password = 'testuser')
        self.second_account = Account.objects.create(name='testAccount', 
                                                balance=0.00, user=self.user)
        self.overdrawn_transaction = Transaction.objects.create(account=self.second_account, amount=-150.00,
                                                            description='test', active=True,
                                                            transaction_date = datetime.datetime.now())

    def test_transaction_list(self):
        self.assertEqual(len(self.second_account.transactions.all()), 1)

    def test2_account_balance_check(self):
        self.assertFalse(self.second_account.check_balance())
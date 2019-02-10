from django.test import TestCase
from fintech.models import Account, Transaction
from django.contrib.auth.models import User
import datetime

class AccountTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testUser', password = 'testuser')
        self.account = Account.objects.create(name='testAccount', 
                                                balance =100.00, user=self.user)
        self.balanced_transaction = Transaction.objects.create(account=self.account, amount=50,
                                                            description='test', active=True,
                                                            transaction_date = datetime.datetime.now())
        self.overdrawn_transaction = Transaction.objects.create(account=self.account, amount=150,
                                                            description='test', active=True,
                                                            transaction_date = datetime.datetime.now()) 

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testUser')

    def test_account_creation(self):
        
        self.assertEqual(self.account.name, 'testAccount')
        self.assertEqual(self.account.balance, 100.00)
        self.assertEqual(self.account.user, self.user)
        self.assertTrue(self.account.uuid)

    def test_str_method(self):
        self.assertEqual(str(self.account), self.account.name)

    def test_transactions(self):
        self.assertEqual(self.balanced_transaction.amount, 50)
        self.assertEqual(self.overdrawn_transaction.description, 'test')

    def test_transaction_overdraw(self):
        self.assertTrue(self.balanced_transaction.check_validity(self.account))
        self.assertFalse(self.overdrawn_transaction.check_validity(self.account)) 

from django.test import TestCase
from fintech.models import Account, Transaction
from django.contrib.auth.models import User

class AccountTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testUser', password = 'testuser')
        self.account = Account.objects.create(name='testAccount', 
                                                balance =100.00, user=self.user)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testUser')

    def test_account_creation(self):
        
        self.assertEqual(self.account.name, 'testAccount')
        self.assertEqual(self.account.balance, 100.00)
        self.assertEqual(self.account.user, self.user)
        self.assertTrue(self.account.uuid)

    def test_str_method(self):
        self.assertEqual(str(self.account), self.account.name)
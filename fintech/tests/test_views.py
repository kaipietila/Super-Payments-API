from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

from fintech import views
from fintech.models import Account

class APIview_tests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testUser', password = 'testuser')
        self.account = Account.objects.create(name='testAccount', 
                                                balance=0.00, user=self.user)
        self.client = Client()

    def test_transaction_list(self):
        """
        testing the endpoint GET api/account/<uuid:uuid>/transactions
        returns a transaction list of the account(uuid)
        """
        #get request
        uuid = self.account.uuid
        response = self.client.get(reverse('fintech:transaction-list', kwargs={'uuid': uuid}))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_bad_transaction_list_request(self):
        """
        testing to get a 404 error fetching with random uuid
        """
        x = uuid.uuid4()
        test_uuid = str(x)
        response = self.client.get(reverse('fintech:transaction-list', kwargs={'uuid': test_uuid}))
        # Check that the response is 404 since the uuid is not matching.
        self.assertEqual(response.status_code, 404)
    
    def test_transaction_post(self):
        pass
        """ uuid = 'a94d387d-2e9f-4a97-9db5-c1696aea1771'
        request = self.client.post(reverse('fintech:transaction-list', kwargs={'uuid': uuid}))"""
    
    def test_account_detail(self):
        """
        testing the endpoint GET api/account/<uuid:uuid>/
        returns the account details of one account based on the uuid
        """
        uuid = self.account.uuid
        response = self.client.get(reverse('fintech:account_detail', kwargs={'uuid': uuid}))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_bad_account_detail_request(self):
        """
        testing to get a 404 error fetching with random uuid
        """
        x = uuid.uuid4()
        test_uuid = str(x)
        response = self.client.get(reverse('fintech:account_detail', kwargs={'uuid': test_uuid}))
        # Check that the response is 404, because uuid is not matching.
        self.assertEqual(response.status_code, 404)

    def test_account_balance(self):
        """
        testing the endpoint GET api/account/<uuid:uuid>/balance
        returns the account details of one account based on the uuid
        """
        uuid = self.account.uuid
        response = self.client.get(reverse('fintech:account_balance', kwargs={'uuid': uuid}))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_bad_account_balance_request(self):
        """
        testing to get a 404 error fetching with random uuid
        """
        x = uuid.uuid4()
        test_uuid = str(x)
        response = self.client.get(reverse('fintech:account_balance', kwargs={'uuid': test_uuid}))
        # Check that the response is 404, because uuid is not matching.
        self.assertEqual(response.status_code, 404)

    
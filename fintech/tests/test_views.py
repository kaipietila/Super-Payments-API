from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

from fintech import views
from fintech.models import Account

#TODO Setup mock accounts etc and try again

class APIview_tests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testUser', password = 'testuser')
        self.account = Account.objects.create(name='testAccount', 
                                                balance=0.00, user=self.user)
        self.client = Client()

    def test_transaction_list(self):
        """
        testing the endpoint GET api/account/<uuid:uuid>/transactions
        """
        #get request
        uuid = self.account.uuid
        response = self.client.get(reverse('fintech:transaction-list', kwargs={'uuid': uuid}))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_bad_transaction_request(self):
        x = uuid.uuid4()
        test_uuid = str(x)
        response = self.client.get(reverse('fintech:transaction-list', kwargs={'uuid': test_uuid}))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 404)

    def test_transaction_post(self):
        pass
        """ uuid = 'a94d387d-2e9f-4a97-9db5-c1696aea1771'
        request = self.client.post(reverse('fintech:transaction-list', kwargs={'uuid': uuid}))"""


    
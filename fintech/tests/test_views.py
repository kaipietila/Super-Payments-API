from django.test import TestCase
from django.test import Client
from django.urls import reverse
from fintech import views

class APIview_tests(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_transaction_list(self):
        """
        testing the endpoint GET api/account/<uuid:uuid>/transactions
        using uuid(a94d387d-2e9f-4a97-9db5-c1696aea1771) of testaccount in db
        """
        #get request
        uuid = 'a94d387d-2e9f-4a97-9db5-c1696aea1771'
        response = self.client.get(reverse('fintech:transaction-list', args=[uuid]))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
from django.core.management.base import BaseCommand
from fintech.models import Account, Transaction
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import datetime
from random import randint
"""
This is a command to load some dummy data to the db.
Use command manage.py create_dummy_data <int> --prefix <string>
The variable will stand for how many accounts you want created
and what kind of prefix you want for the account names, to be able to 
differentiate them from the other users.
Default will be one and will create 1 User with 1 Account with 
10 Transactions.
"""

class Command(BaseCommand):
    help = "create x amount of dummy profiles to the database"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help="indicates how many users you want created")

        parser.add_argument('--prefix', type=str, help='add a prefix to the usernames')


    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        for i in range(total):
            random_string = get_random_string(length=5)
            user = User.objects.create_user(username=f'{prefix}_{random_string}', password=123,)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))
            account = Account.objects.create(name=random_string, balance=0.00, user=user)
            self.stdout.write(self.style.SUCCESS(f'Successfully created account {account.name}'))
            for j in range(10):
                date = datetime.date.today()
                amount = randint(1,50)
                Transaction.objects.create(account=account, transaction_date=date, amount=amount,
                                            description=f'{random_string}_{j}', active=True)
                self.stdout.write(self.style.SUCCESS('Successfully created transaction'))

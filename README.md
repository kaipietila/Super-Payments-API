Holvi transaction API exercise 
==============================

Welcome to The Super Payments API!
For the API documentation you can go to http://127.0.0.1:8000/docs/

Setup:
--------------------
Install dependencies from requirements.txt. 
Run with command 'manage.py runserver'

To populate the DB with some test users, accounts, transactions you
can user the command <strong>manage.py create_dummy_data (int) --prefix (string)</strong>.
Int represents total amount of users to create. Each user will get one account
and 10 payments. --prefix will add some prefix to the randomly generated username
so that test users can be easily differentiated.

Running:
--------------
When server running you can refer to the API docs <a href=http://127.0.0.1:8000/docs/> here!</a>

From the different endpoints you can: 
   1. Get account detail information(GET account/uuid/)
   2. Get account balance details(GET account/uuid/balance)
   3. Get all transactions for the account (GET account/uuid/transactions)
   4. Create a new transaction (POST account/uuid/transactions)

Tests:
--------------
Testing is done with the django built in testing framework.
To test run e.g manage.py test fintech.tests 

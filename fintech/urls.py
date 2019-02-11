from django.urls import path
from fintech import views

app_name = 'fintech'

urlpatterns = [
    path('account/<uuid:uuid>/transactions', views.TransactionList.as_view()),

]
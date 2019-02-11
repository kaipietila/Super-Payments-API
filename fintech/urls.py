from django.urls import path
from fintech import views

app_name = 'fintech'

urlpatterns = [
    path('account/<uuid:uuid>/transactions', views.TransactionList.as_view()),
    path('account/<uuid:uuid>/', views.AccountDetail.as_view()),
    path('account/<uuid:uuid>/balance/', views.AccountBalanceDetails.as_view())


]
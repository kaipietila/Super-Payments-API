from rest_framework import viewsets
from django.contrib.auth.models import User
from user_management.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


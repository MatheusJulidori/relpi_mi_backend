# *coding: utf-8*
from accounts.models import User
from api.serializers import *
from rest_framework import generics
class UserListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
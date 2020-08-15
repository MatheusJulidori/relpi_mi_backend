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

class ClientListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class HelperListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Helper.objects.all()
    serializer_class = HelperSerializer

class PedidosListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


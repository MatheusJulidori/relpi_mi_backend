# *coding: utf-8*
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from api.serializers import *
from rest_framework import generics, status, permissions


class LoginListView(APIView):

    permission_classes = (permissions.AllowAny,)
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     queryset = self.get_queryset().filter()
    #     serializer = UserSerializer(queryset, many=False)
    #     return Response(serializer.data)

    # def get(selfself, request, format=None):
    #     return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            password = request.data.get('password', None)
            email = request.data.get('email', None)
            qs = User.objects.filter()
            results = {'test': '1', 'email': 'as@gamial'}

            return Response(data=results, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class UserListView(generics.ListAPIView):
#     """
#             get:
#                 Search or get users
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class ClientListView(generics.ListAPIView):
#     """
#             get:
#                 Search or get users
#     """
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class HelperListView(generics.ListAPIView):
#     """
#             get:
#                 Search or get users
#     """
#     queryset = Helper.objects.all()
#     serializer_class = HelperSerializer

# class PedidosListView(generics.ListAPIView):
#     """
#             get:
#                 Search or get users
#     """
#     queryset = Pedidos.objects.all()
#     serializer_class = PedidosSerializer


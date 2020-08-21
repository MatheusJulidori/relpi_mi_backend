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

    def get(selfself, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            password = request.data.get('password', None)
            email = request.data.get('email', None)
            qs = User.objects.filter(email=email, password=password).values()
            if not qs:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            #results = {'data': qs}
            return Response(data=qs, status=status.HTTP_200_OK)
            #return Response(data=results, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterListView(generics.CreateAPIView):
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




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


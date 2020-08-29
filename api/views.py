# *coding: utf-8*
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from api.serializers import *
from rest_framework import generics, status, permissions
from relpi_miAPP.models import Pedidos




class CancelListView(APIView):
    def post (self, request):
        id = request.data.get('id', None)
        email_helper = request.data.get('email_client', None)
        email = Pedidos.objects.filter(id=id).values('email_client')
        if email == email_helper:
            cancelado = Pedidos.objects.filter(id=id).update(cancelado = True)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class FinishListView(APIView):
    def post (self, request):
        id = request.data.get('id', None)
        email_helper = request.data.get('email_helper', None)
        email = Pedidos.objects.filter(id=id).values('email_helper')
        if email == email_helper:
            finalizado = Pedidos.objects.filter(id=id).update(terminado = True)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)




class DetailsListView(APIView):
    def post (self,request):
        id = request.data.get('id', None)
        queryset = Pedidos.objects.filter(id=id).values()
        return Response(data=queryset,status=status.HTTP_200_OK)

class MyClientListView(APIView):

    def post(self,request):
        email_client = request.data.get('email_client', None)
        queryset = Pedidos.objects.filter(email_client=email_client).values('helper_name','task_name','id')
        return Response(data=queryset,status=status.HTTP_200_OK)

class MyHelperListView(APIView):

    def post(self,request):
        email_helper = request.data.get('email_helper', None)
        queryset = Pedidos.objects.filter(email_helper=email_helper).values('client_name','task_name','id')
        return Response(data=queryset,status=status.HTTP_200_OK)


class AjudarListView(APIView):

    def post(self,request):
        id = request.data.get('id',None)
        helper_name = request.data.get('helper_name', None)
        email_helper = request.data.get('email_helper', None)
        helper_phone = request.data.get('helper_phone', None)
        Pedidos.objects.filter(id=id).update(helper_name=helper_name,email_helper=email_helper,helper_phone=helper_phone,is_taken=True)
        return Response(status=status.HTTP_200_OK)



class PostarListView(generics.CreateAPIView): #APIView
    # def post(self,request):
    #     description = request.data.get('description',None)
    #    payment = request.data.get('payment', None)
    #     pago = request.data.get('pago', None)
    #     email_client = request.data.get('email_client', None)
    #     email_helper = request.data.get('email_helper', None)
    #     client_name = request.data.get('client_name', None)
    #     client_phone = request.data.get('client_phone', None)
    #     helper_name = request.data.get('helper_name', None)
    #     helper_phone = request.data.get('helper_phone', None)
    #     task_name = request.data.get('task_name', None)

        serializer_class = PedidosSerializer

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class AvailableListView(APIView):
    def get(self,request,format=None):
        queryset=Pedidos.objects.filter(is_taken=False).values('task_name','description','id')
        return Response(data=queryset,status=status.HTTP_200_OK)



class LoginListView(APIView):

    permission_classes = (permissions.AllowAny,)
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     queryset = self.get_queryset().filter()
    #     serializer = UserSerializer(queryset, many=False)
    #     return Response(serializer.data)

    def get(self, request, format=None):
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


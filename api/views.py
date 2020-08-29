# *coding: utf-8*
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from api.serializers import *
from rest_framework import generics, status, permissions
from relpi_miAPP.models import Pedidos




class CancelListView(APIView):
    def post (self, request):
        try:
            id = request.data.get('id', None)
            email_helper = request.data.get('email_client', None)
            email = Pedidos.objects.filter(id=id).values('email_client')
            if email == email_helper:
                Pedidos.objects.filter(id=id).update(cancelado = True)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FinishListView(APIView):
    def post (self, request):
        try:
            id = request.data.get('id', None)
            email_helper = request.data.get('email_helper', None)
            email = Pedidos.objects.filter(id=id).values('email_helper')
            #if email == email_helper:
            Pedidos.objects.filter(id=id).update(terminado = True)
            return Response(status=status.HTTP_200_OK)
            #else:
                #return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DetailsListView(APIView):
    def post (self,request):
        id = request.data.get('id', None)
        queryset = Pedidos.objects.filter(id=id).values()
        return Response(data=queryset,status=status.HTTP_200_OK)

class MyClientListView(APIView):

    def post(self,request):
        try:
            email_client = request.data.get('email_client', None)
            queryset = Pedidos.objects.filter(email_client=email_client).values()
            return Response(data=queryset,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MyHelperListView(APIView):

    def post(self,request):
        try:
            email_helper = request.data.get('email_helper', None)
            queryset = Pedidos.objects.filter(email_helper=email_helper).values()
            return Response(data=queryset,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AjudarListView(APIView):

    def post(self,request):
        try:
            id = request.data.get('id',None)
            helper_name = request.data.get('helper_name', None)
            email_helper = request.data.get('email_helper', None)
            helper_phone = request.data.get('helper_phone', None)
            Pedidos.objects.filter(id=id).update(helper_name=helper_name,email_helper=email_helper,helper_phone=helper_phone,is_taken=True)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PostarListView(generics.CreateAPIView): #APIView
    # def post(self,request):

        serializer_class = PedidosSerializer

        def create(self, request, *args, **kwargs):
            try:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AvailableListView(APIView):
    def get(self,request,format=None):
        try:
            queryset=Pedidos.objects.filter(is_taken=False).values()
            return Response(data=queryset,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginListView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            password = request.data.get('password', None)
            email = request.data.get('email', None)
            qs = User.objects.filter(email=email, password=password).values()
            if not qs:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            return Response(data=qs, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterListView(generics.CreateAPIView):
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api.views import *

urlpatterns = [
    # path('users/', UserListView.as_view(), name='users_list'),
    # path('clients/', ClientListView.as_view(), name='clients_list'),
    # path('helpers/', HelperListView.as_view(), name='helpers_list'),
    # path('pedidos/', PedidosListView.as_view(), name='pedidos_list'),
    path('', include(router.urls)),

    path('login/', LoginListView.as_view(), name='login_list'),
    path('register/', RegisterListView.as_view(), name='register_list'),
    path('postarPedido/', PostarListView.as_view(), name='register_task'), #Post
    path('available/', AvailableListView.as_view(), name='available_tasks'), #Get
    path('ajudar/', AjudarListView.as_view(), name='take_task'), #Post
    path('mytask_helper/', MyHelperListView.as_view(), name='helper_tasks'), #Post
    path('mytask_client/', MyClientListView.as_view(), name = 'client_tasks'), #Post
    # path('task_details/', DetailsListView.as_view(), name = 'task_detail'), #Post

]


from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api.views import *
urlpatterns = [
    path('users/', UserListView.as_view(), name='users_list'),
    path('', include(router.urls))
]

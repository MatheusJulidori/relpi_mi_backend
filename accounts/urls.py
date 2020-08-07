from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup),
    path('logout/', views.logout_request),
]

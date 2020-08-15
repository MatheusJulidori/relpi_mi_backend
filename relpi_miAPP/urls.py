from django.urls import path
from . import views
#from relpi_miBE import relpi_miAPP

urlpatterns = [
    path('', views.index, name='home'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]
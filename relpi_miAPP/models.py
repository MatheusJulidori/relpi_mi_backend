from django.db import models
from accounts.models import Client,Helper
from django.contrib import admin

class Pedidos(models.Model):
    email_client = models.CharField(max_length = 254)
    client_name = models.CharField(max_length = 254)
    client_phone = models.CharField(max_length = 254)
    is_taken = models.BooleanField(verbose_name='is_taken',default = False)
    email_helper = models.CharField(max_length = 254, default = 'a')
    helper_name = models.CharField(max_length = 254, blank = False, default = 'a')
    helper_phone = models.CharField(max_length = 254, blank = False, default = 'a')
    task_name = models.CharField(max_length = 254, blank = False)
    description = models.TextField(verbose_name='description')
    payment = models.CharField(verbose_name='payment', max_length=1)
    pago = models.BooleanField(verbose_name='pago',default = False)

    def __str__(self):
        return str(self.task_name)

admin.site.register(Pedidos)

from django.db import models
from accounts.models import User
from django.contrib import admin

class Pedidos(models.Model):
    email_client = models.ForeignKey(User,on_delete=models.CASCADE) #User client
    is_taken = models.BooleanField(verbose_name='is_taken')
   # email_helper = models.ForeignKey(verbose_name='email_helper',User,on_delete=models.CASCADE) #User helper
    description = models.TextField(verbose_name='description')
    payment = models.CharField(verbose_name='payment', max_length=1)
    pago = models.BooleanField(verbose_name='pago')

admin.site.register(Pedidos)
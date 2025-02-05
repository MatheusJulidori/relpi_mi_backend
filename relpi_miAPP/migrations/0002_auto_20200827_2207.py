# Generated by Django 3.0.8 on 2020-08-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relpi_miAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='client_name',
            field=models.CharField(default='a', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidos',
            name='client_phone',
            field=models.CharField(default='a', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidos',
            name='helper_name',
            field=models.CharField(default='a', max_length=254),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='helper_phone',
            field=models.CharField(default='a', max_length=254),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='task_name',
            field=models.CharField(default='a', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='email_client',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='email_helper',
            field=models.CharField(default='a', max_length=254),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='is_taken',
            field=models.BooleanField(default=False, verbose_name='is_taken'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='pago',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
    ]

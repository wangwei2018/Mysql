# Generated by Django 2.1.1 on 2018-09-19 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_auto_20180919_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_imp',
            name='time',
        ),
        migrations.RemoveField(
            model_name='order_new',
            name='time',
        ),
        migrations.RemoveField(
            model_name='order_send',
            name='time',
        ),
    ]

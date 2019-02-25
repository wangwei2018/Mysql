# Generated by Django 2.1.1 on 2018-09-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0005_auto_20180919_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_imp',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='时间'),
        ),
        migrations.AddField(
            model_name='order_new',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='时间'),
        ),
        migrations.AddField(
            model_name='order_send',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='order_imp',
            name='status',
            field=models.IntegerField(choices=[(0, '等待接单'), (1, '正在处理'), (2, '完成')], default=0, max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='order_new',
            name='status',
            field=models.IntegerField(choices=[(0, '等待接单'), (1, '正在处理'), (2, '完成')], default=0, max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='order_send',
            name='status',
            field=models.IntegerField(choices=[(0, '等待接单'), (1, '正在处理'), (2, '完成')], default=0, max_length=20, verbose_name='状态'),
        ),
    ]
# Generated by Django 2.1.1 on 2018-09-18 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('ca_name', models.CharField(max_length=50, verbose_name='名称')),
            ],
            options={
                'verbose_name': '软件类别',
                'verbose_name_plural': '软件类别',
            },
        ),
        migrations.CreateModel(
            name='Image_imp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('url', models.CharField(max_length=200, verbose_name='图片链接')),
            ],
            options={
                'verbose_name': '改良应用图片链接',
                'verbose_name_plural': '改良应用图片链接',
            },
        ),
        migrations.CreateModel(
            name='Image_new',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('url', models.CharField(max_length=200, verbose_name='图片链接')),
            ],
            options={
                'verbose_name': '新应用图片链接',
                'verbose_name_plural': '新应用图片链接',
            },
        ),
        migrations.CreateModel(
            name='Image_old',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('url', models.CharField(max_length=200, verbose_name='图片链接')),
            ],
            options={
                'verbose_name': '原应用图片链接',
                'verbose_name_plural': '原应用图片链接',
            },
        ),
        migrations.CreateModel(
            name='Order_imp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.CharField(max_length=1000, verbose_name='简介')),
                ('require', models.CharField(max_length=200, verbose_name='需求')),
                ('platform', models.CharField(max_length=100, verbose_name='使用平台')),
                ('price', models.IntegerField(verbose_name='单价')),
                ('count', models.IntegerField(verbose_name='使用人数')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Order_new',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('url', models.CharField(max_length=200, null=True, verbose_name='源码链接')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.CharField(max_length=1000, verbose_name='简介')),
                ('require', models.CharField(max_length=200, verbose_name='需求')),
                ('platform', models.CharField(max_length=100, verbose_name='使用平台')),
                ('price', models.IntegerField(verbose_name='单价')),
                ('count', models.IntegerField(verbose_name='使用人数')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_new', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Order_send',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('url', models.CharField(max_length=200, verbose_name='源码链接')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.CharField(max_length=1000, verbose_name='简介')),
                ('require', models.CharField(max_length=200, verbose_name='需求')),
                ('platform', models.CharField(max_length=100, verbose_name='使用平台')),
                ('price', models.IntegerField(verbose_name='单价')),
                ('count', models.IntegerField(verbose_name='使用人数')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_send', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Software_imp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('imp_name', models.CharField(max_length=100, verbose_name='名称')),
                ('product', models.CharField(max_length=100, verbose_name='生产商')),
                ('difference', models.CharField(max_length=1000, verbose_name='不同')),
                ('price', models.IntegerField(verbose_name='单价')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='software_imp', to='software.Category', verbose_name='类别名称')),
            ],
            options={
                'verbose_name': '市面上已有的应用的改良应用',
                'verbose_name_plural': '市面上已有的应用的改良应用',
            },
        ),
        migrations.CreateModel(
            name='Software_new',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('new_name', models.CharField(max_length=100, verbose_name='名称')),
                ('product', models.CharField(max_length=100, verbose_name='生产商')),
                ('description', models.CharField(max_length=1000, verbose_name='简介')),
                ('platform', models.CharField(max_length=100, verbose_name='使用平台')),
                ('price', models.IntegerField(verbose_name='单价')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='software_new', to='software.Category', verbose_name='类别名称')),
            ],
            options={
                'verbose_name': '全新定制应用',
                'verbose_name_plural': '全新定制应用',
            },
        ),
        migrations.CreateModel(
            name='Software_old',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('old_name', models.CharField(max_length=100, verbose_name='名称')),
                ('product', models.CharField(max_length=100, verbose_name='生产商')),
                ('description', models.CharField(max_length=1000, verbose_name='简介')),
                ('platform', models.CharField(max_length=100, verbose_name='使用平台')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='software_old', to='software.Category', verbose_name='类别名称')),
            ],
            options={
                'verbose_name': '市面上已有的应用，且拥有源码',
                'verbose_name_plural': '市面上已有的应用，且拥有源码',
            },
        ),
        migrations.CreateModel(
            name='SoundCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('url', models.CharField(max_length=200, verbose_name='源码链接')),
            ],
            options={
                'verbose_name': '原应用源码链接',
                'verbose_name_plural': '原应用源码链接',
            },
        ),
        migrations.AddField(
            model_name='software_old',
            name='sound_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='software_old', to='software.SoundCode', verbose_name='改良应用订单'),
        ),
        migrations.AddField(
            model_name='software_new',
            name='sound_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='software_new', to='software.SoundCode', verbose_name='改良应用订单'),
        ),
        migrations.AddField(
            model_name='software_imp',
            name='oldsoft_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='software_imp', to='software.Software_old', verbose_name='原应用'),
        ),
        migrations.AddField(
            model_name='software_imp',
            name='sound_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='software_imp', to='software.SoundCode', verbose_name='改良应用订单'),
        ),
        migrations.AddField(
            model_name='order_imp',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='software.Software_old', verbose_name='应用'),
        ),
        migrations.AddField(
            model_name='order_imp',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_imp', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='image_old',
            name='software_oldId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imgs', to='software.Software_old', verbose_name='应用'),
        ),
        migrations.AddField(
            model_name='image_new',
            name='software_newId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imgs', to='software.Software_new', verbose_name='应用'),
        ),
        migrations.AddField(
            model_name='image_imp',
            name='software_impId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imgs', to='software.Software_imp', verbose_name='应用'),
        ),
    ]

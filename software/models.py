from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 软件类别
class Category(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    ca_name = models.CharField(max_length=50, verbose_name="名称")

    class Meta:
        verbose_name = "软件类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ca_name


class SoundCode(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    url = models.CharField(max_length=200, verbose_name="源码链接")

    class Meta:
        verbose_name = "原应用源码链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


# 市面上已经有的软件，且有源代码
class Software_old(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    old_name = models.CharField(max_length=100, verbose_name="名称")
    product = models.CharField(max_length=100, verbose_name="生产商")
    description = models.CharField(max_length=1000, verbose_name="简介")
    platform = models.CharField(max_length=100, verbose_name="使用平台")
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="software_old",
                                    verbose_name="类别名称")

    sound_code = models.OneToOneField(SoundCode, on_delete=models.PROTECT, related_name="software_old",
                                      verbose_name="改良应用订单")

    class Meta:
        verbose_name = "市面上已有的应用，且拥有源码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.old_name


# 市面上已经有的软件进行的改良软件
class Software_imp(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    imp_name = models.CharField(max_length=100, verbose_name="名称")
    product = models.CharField(max_length=100, verbose_name="生产商")
    difference = models.CharField(max_length=1000, verbose_name="不同")
    price = models.IntegerField(verbose_name="单价")
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="software_imp",
                                    verbose_name="类别名称")
    oldsoft_id = models.ForeignKey(Software_old, on_delete=models.PROTECT, related_name="software_imp",
                                   verbose_name="原应用")

    sound_code = models.OneToOneField(SoundCode, on_delete=models.PROTECT, related_name="software_imp",
                                      verbose_name="改良应用订单")

    class Meta:
        verbose_name = "市面上已有的应用的改良应用"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.imp_name


# 全新定制的应用
class Software_new(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    new_name = models.CharField(max_length=100, verbose_name="名称")
    product = models.CharField(max_length=100, verbose_name="生产商")
    description = models.CharField(max_length=1000, verbose_name="简介")
    platform = models.CharField(max_length=100, verbose_name="使用平台")
    price = models.IntegerField(verbose_name="单价")
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="software_new",
                                    verbose_name="类别名称")

    sound_code = models.OneToOneField(SoundCode, on_delete=models.PROTECT, related_name="software_new",
                                      verbose_name="改良应用订单")

    class Meta:
        verbose_name = "全新定制应用"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.new_name


class Image_old(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    url = models.CharField(max_length=200, verbose_name="图片链接")
    software_oldId = models.ForeignKey(Software_old, on_delete=models.PROTECT, related_name="imgs", verbose_name="应用")

    class Meta:
        verbose_name = "原应用图片链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


class Image_imp(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    url = models.CharField(max_length=200, verbose_name="图片链接")
    software_impId = models.ForeignKey(Software_imp, on_delete=models.PROTECT, related_name="imgs", verbose_name="应用")

    class Meta:
        verbose_name = "改良应用图片链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


class Image_new(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    url = models.CharField(max_length=200, verbose_name="图片链接")
    software_newId = models.ForeignKey(Software_new, on_delete=models.PROTECT, related_name="imgs", verbose_name="应用")

    class Meta:
        verbose_name = "新应用图片链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


class Order_imp(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)

    name = models.CharField(max_length=100, verbose_name="名称")
    description = models.CharField(max_length=1000, verbose_name="简介")
    require = models.CharField(max_length=200, verbose_name="需求")
    platform = models.CharField(max_length=100, verbose_name="使用平台")
    price = models.IntegerField(verbose_name="单价", null=True)
    count = models.IntegerField(verbose_name="使用人数")

    status = models.IntegerField(verbose_name="状态", default=0,
                                 choices=((0, "等待接单"), (1, "正在处理"), (2, "完成")))

    time = models.DateTimeField(auto_now=True, verbose_name="时间")

    software = models.ForeignKey(Software_old, on_delete=models.PROTECT, related_name="order", verbose_name="应用")

    user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order_imp", verbose_name="用户")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Order_send(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)

    url = models.CharField(max_length=200, verbose_name="源码链接")

    name = models.CharField(max_length=100, verbose_name="名称")
    description = models.CharField(max_length=1000, verbose_name="简介")
    require = models.CharField(max_length=200, verbose_name="需求")
    platform = models.CharField(max_length=100, verbose_name="使用平台")
    count = models.IntegerField(verbose_name="使用人数")

    time = models.DateTimeField(auto_now=True, verbose_name="时间")

    status = models.IntegerField(verbose_name="状态", default=0,
                                 choices=((0, "等待接单"), (1, "正在处理"), (2, "完成")))

    user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order_send", verbose_name="用户")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Order_new(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)

    url = models.CharField(max_length=200, verbose_name="源码链接", null=True)

    name = models.CharField(max_length=100, verbose_name="名称")
    description = models.CharField(max_length=1000, verbose_name="简介")
    require = models.CharField(max_length=200, verbose_name="需求")
    platform = models.CharField(max_length=100, verbose_name="使用平台")
    price = models.IntegerField(verbose_name="单价", null=True)
    count = models.IntegerField(verbose_name="使用人数")

    time = models.DateTimeField(auto_now=True, verbose_name="时间")

    status = models.IntegerField(verbose_name="状态", default=0,
                                 choices=((0, "等待接单"), (1, "正在处理"), (2, "完成")))

    user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order_new", verbose_name="用户")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

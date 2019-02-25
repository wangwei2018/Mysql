from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Order_send
import os
import shutil


@login_required
def improve(request):
    if request.method == "GET":
        return render(request, "software/select.html")
    elif request.method == "POST":
        value = request.POST.get("choice")
        if value == "first":
            return HttpResponseRedirect("/software/sendcode/")
        else:
            return HttpResponseRedirect("/software/upgrade/")


@login_required
def sendcode(request):
    if request.method == "GET":
        return render(request, "software/sendcode.html")
    elif request.method == "POST":
        softname = request.POST.get("softname")
        platform = request.POST.get("platform")
        count = request.POST.get("count")
        softsituation = request.POST.get("softsituation")
        softrequire = request.POST.get("softrequire")
        order = Order_send()
        order.name = softname
        order.platform = platform
        order.count = count
        order.description = softsituation
        order.require = softrequire
        order.user_id = request.user
        if not request.session.get("id"):
            request.session["id"] = 1
        order.url = "/home/ww/file/app/" + str(request.user.id) + "/" + str(
            request.session["id"]) + "/" + softname + ".rar"
        order.save()
        request.session["id"] = order.id + 1
        return HttpResponseRedirect("/software/mycar/")


@login_required
def upgratesoft(request):
    if request.method == "GET":
        return render(request, "software/upgradesoft.html")


@login_required
def save(request):
    if request.method == "POST":
        file = request.FILES.get('file')

        if request.session.get("id"):
            id = request.session.get("id")
        else:
            id = 1

        user = request.user
        path = "/home/ww/app/file/" + str(user.id) + "/" + str(id)
        folder = os.path.exists(path)
        if folder:
            shutil.rmtree(path)
        os.makedirs(path)

        tool = open(path + "/" + file.name, "wb")
        for chunk in file.chunks():
            tool.write(chunk)

        tool.close()

        return HttpResponseRedirect("/software/mycar/")


@login_required
def myorder(request):
    content = {}
    user = request.user
    order_send = user.order_send.filter(status=0).order_by("time").reverse()
    content["order_send"] = order_send
    order_imp = user.order_imp.filter(status=0).order_by("time").reverse()
    content["order_imp"] = order_imp
    order_new = user.order_new.filter(status=0).order_by("time").reverse()
    content["order_new"] = order_new
    return render(request, "software/myorder.html", context=content)

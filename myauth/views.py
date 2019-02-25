from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def auth_login(request):
    content = {}
    if request.method == "GET":
        message = request.GET.get("message")
        if message:
            content["message"] = message
        return render(request, "myauth/login.html", context=content)
    elif request.method == "POST":
        username = request.POST.get("account")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            next = request.GET.get("next")
            if next and len(next) > 0:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect("/index/")
        else:
            content["error"] = "用户名或密码错误"
            return render(request, "myauth/login.html", context=content)


def auth_register(request):
    if request.method == "GET":
        return render(request, "myauth/register.html")
    elif request.method == "POST":
        content = {}
        username = request.POST.get("account")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if len(User.objects.filter(username=username)) > 0:
            content["error"] = "用户名已经被注册"
            return render(request, "myauth/register.html", context=content)
        elif len(User.objects.filter(email=email)) > 0:
            content["error"] = "邮箱已经被注册"
            return render(request, "myauth/register.html", context=content)
        else:
            user = User()
            user.username = username
            user.set_password(password)
            user.email = email
            user.save()
            message = "注册成功，请登录"
            return HttpResponseRedirect("auth/login/?message=" + message)


@login_required
def auth_logout(request):
    logout(request)
    message = "注销成功，请重新登录"
    return HttpResponseRedirect("auth/login/?message=" + message)

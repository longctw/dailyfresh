# coding=utf-8

from django.shortcuts import *
from .models import *
from hashlib import sha1
from django.http import JsonResponse


# Create your views here.
def register(request):
    context = {'title': 'User Register'}
    return render(request, 'df_user/register.html', context)


def login(request):
    user = UserInfo()
    user.uname = request.COOKIES.get('username', '')
    print(user.uname + '----............')
    context = {'title': 'User Login', 'user_info': user}
    return render(request, 'df_user/login.html', context)


def register_handle(request):
    # revecier user input
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    upwd2 = post.get("cpwd")
    uemail = post.get("email")

    # compare weather the two password are consistent
    if upwd != upwd2:

        return redirect("/user/register")

    # encrypt the password
    s1 = sha1()
    s1.update(upwd.encode("utf8"))
    upwd3 = s1.hexdigest()

    # build UserInfo Object, and save to db
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # redirect to login page
    return redirect("/user/login")


def login_handle(request):
    post_data = request.POST
    u_name = post_data.get('username')
    pwd = post_data.get('pwd')
    remember = post_data.get('remember', '0')
    users = UserInfo.objects.filter(uname=u_name)
    user_info = {'uname': u_name, 'pwd':pwd}

    if len(users) < 1:
        context = {'title': 'User Login', 'name_error': 'Username is not exist, please check!', 'user_info': user_info}
        return render(request, 'df_user/login.html', context)

    user = users[0]
    # encrypt the password
    s1 = sha1()
    s1.update(pwd.encode("utf8"))
    encrypt_pwd = s1.hexdigest()

    if user.upwd != encrypt_pwd:
        context = {'title': 'User Login', 'pwd_error': 'Password error, please check!', 'user_info': user_info}
        return render(request, 'df_user/login.html', context)

    resp = HttpResponseRedirect('/user/info')

    if remember == '1':
        resp.set_cookie('username', u_name)
    else:
        resp.set_cookie('username', '', max_age=-1)

    request.session['user_info'] = user.uname
    return resp


def uname_repeated(request):
    getData = request.GET
    uname = getData.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def user_info(request):
    context = {'title': 'User Center'}
    return render(request, 'df_user/user_center_info.html', context)
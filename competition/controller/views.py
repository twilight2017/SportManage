from django.shortcuts import render
from .models import Students, Admins
from django.shortcuts import render, redirect
from django.contrib.auth import login as LOGIN, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

# Create your views here.


def register(request):
    result = ''
    if request.method == "POST" and request.POST:
        # 判断是否为POST请求
        # i_identity = request.POST.get('identity')
        # if i_identity == "参赛人员":
            u_id = request.POST.get('stu_id')
            u_name = request.POST.get('stu_name')
            u_gender = request.POST.get('stu_gender')
            u_college = request.POST.get('stu_college')
            u_identity = request.POST.get('identity')
            u_mail = request.POST.get('stu_mail')
            u_password = request.POST.get('stu_password')
            u_pass = request.POST.get('stu_pass')
            if u_password == u_pass:
                db = Students.objects.filter(stu_id=u_id)
                if db:
                    result = 'had'
                    # 该用户用户已注册过
                    return render(request, 'register.html', {'result': result})
                else:
                    if u_identity == "1":
                        info = Students()
                        info.stu_id = u_id
                        info.stu_name = u_name
                        info.stu_gender = u_gender
                        info.identity = u_identity
                        info.stu_college = u_college
                        info.stu_mail = u_mail
                        info.stu_password = u_password
                        info.save()
                        result = 'success'
                        return render(request, 'register.html', {'result': result})
                    else:
                        info = Admins()
                        info.adm_id = u_id
                        info.adm_name = u_name
                        info.adm_gender = u_gender
                        info.identity = u_identity
                        info.adm_college = u_college
                        info.adm_mail = u_mail
                        info.adm_password = u_password
                        info.save()
                        result = 'success'
                        return render(request, 'register.html', {'result': result})
            else:
                result = 'error'
                return render(request, 'register.html', {'result': result})
    return render(request, 'register.html', {'result': result})


def login(request):

    if request.method == "POST" and request.POST:
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        try:
            user = User.objects.get(username=_username)
        except User.DoesNotExist:
            user = User()
            user.username = _username
            pwd = make_password(_password)
            user.password = pwd
            user.save()
        # 校验用户
        user = authenticate(username=_username, password=_password)
        if user:
            if _username[0] == 'a':
                LOGIN(request, user)
                adm = Admins.objects.get(adm_name=_username)
                request.session['name'] = adm.adm_name
                request.session['id'] = adm.adm_id
                return redirect('/admhome/')
            else:
                LOGIN(request, user)
                stu = Students.objects.get(stu_name=_username)
                request.session['name'] = stu.stu_name
                request.session['id'] = stu.stu_id
                return redirect('/home/')
        else:
            return render(request, 'login.html', {'error': '用户名或者密码错误！'})
    return render(request, 'login.html')


# Student Home Page
def home(request):
    _name = request.session.get('name')
    _id = request.session.get('id')
    return render(request, 'home.html', {'name': _name, 'id': _id})


# Admin Home Page
def admhome(request):
    _name = request.session.get('name')
    _id = request.session.get('id')
    return render(request, 'admhome.html')

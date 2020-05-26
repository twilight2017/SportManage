from django.shortcuts import render
from .models import Students, Admins, Competitions
from django.shortcuts import render, redirect
from django.contrib.auth import login as LOGIN
from django.contrib.auth import logout as LOGOUT
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

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST" and request.POST:
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
                request.session['gender'] = adm.adm_gender
                request.session['college'] = adm.adm_college
                request.session['mail'] = adm.adm_mail
                return redirect('/admhome/')
            else:
                LOGIN(request, user)
                stu = Students.objects.get(stu_name=_username)
                request.session['name'] = stu.stu_name
                request.session['id'] = stu.stu_id
                request.session['gender'] = stu.stu_gender
                request.session['college'] = stu.stu_college
                request.session['mail'] = stu.stu_mail
                return redirect('/home/')
        else:
            return render(request, 'login.html', {'error': '用户名或者密码错误！'})
    return render(request, 'login.html')


# logout
def logout(request):
    # 不由用户操作的默认session失效时间为2周
    LOGOUT(request)
    return redirect('/')  # 返回登录页面

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


# Student private information
def private(request):
    _name = request.session.get('name')
    _id = request.session.get('id')
    _gender = request.session.get('gender')
    if _gender == "1":
        _gender = "女"
    else:
        _gender = "男"
    _college = request.session.get('college')
    if _college == "0":
        _college = "土木与环境工程学院"
    elif _college == "1":
        _college = "材料科学与工程学院"
    elif _college == "2":
        _college = "机械工程学院"
    elif _college == "3":
        _college = "计算机与通信工程学院"
    elif _college == "4":
        _college = "自动化学院"
    elif _college == "5":
        _college = "数理学院"
    elif _college == "6":
        _college = "化学与生物工程学院"
    elif _college == "7":
        _college = "东凌经济管理学院"
    elif _college == "8":
        _college = "文法学院"
    elif _college == "9":
        _college = "外国语学院"
    else:
        _college = "马克思主义学院"
    _mail = request.session.get('mail')
    return render(request, 'private.html', {'name': _name, 'id': _id, 'gender': _gender, 'college': _college, 'mail': _mail})


# Admain private information
def admprivate(request):
    _name = request.session.get('name')
    _id = request.session.get('id')
    _gender = request.session.get('gender')
    if _gender == "1":
        _gender = "女"
    else:
        _gender = "男"
    _college = request.session.get('college')
    if _college == "0":
        _college = "土木与环境工程学院"
    elif _college == "1":
        _college = "材料科学与工程学院"
    elif _college == "2":
        _college = "机械工程学院"
    elif _college == "3":
        _college = "计算机与通信工程学院"
    elif _college == "4":
        _college = "自动化学院"
    elif _college == "5":
        _college = "数理学院"
    elif _college == "6":
        _college = "化学与生物工程学院"
    elif _college == "7":
        _college = "东凌经济管理学院"
    elif _college == "8":
        _college = "文法学院"
    elif _college == "9":
        _college = "外国语学院"
    else:
        _college = "马克思主义学院"
    _mail = request.session.get('mail')
    return render(request, 'admprivate.html', {'name': _name, 'id': _id, 'gender': _gender, 'college': _college, 'mail': _mail})



def create_com(request):
    result = ''
    if (request.method == "POST" or request.method == "GET") and request.POST:
        c_name = request.POST.get('com_name')
        c_start = request.POST.get('com_start')
        c_end = request.POST.get('com_end')
        c_type = request.POST.get('com_type')
        c_college = request.POST.get('com_college')
        db = Competitions.objects.filter(com_name=c_name)
        if db:
            result = 'had'
            return render(request, 'admadd.html', {'result': result})
        else:
            info = Competitions()
            info.com_name = c_name
            info.com_startime = c_start
            info.com_endtime = c_end
            info.com_type = c_type
            info.com_college = c_college
            info.save()
            result = 'success'
            return redirect('/admdeliver/')
    return render(request, 'admadd.html', {'result': result})


# 展示已经发布的比赛
def admdeliver(request):
     if request.method == 'GET':
         LIST = []  # 用于获取后端所有竞赛信息的列表
         k = Competitions.objects.filter()
         for i in k:
             LIST.append(i)
         return render(request, 'admdeliver.html', {'deliever_list': LIST})


# delete competition
def delete(request, del_name):
    Competitions.objects.filter(com_name=del_name).delete()
    return redirect('/admdeliver/')


#  学生端展示已经发布的比赛
def deliver(request):
    LIST = []  # 用于获取后端所有竞赛信息的列表
    if request.method == 'GET' :
        k = Competitions.objects.filter()
        for i in k:
            LIST.append(i)
        return render(request, 'choice.html', {'choice_list': LIST})


#  学生加入一个比赛
def join(request, join_name):
        u_id = request.session.get('id')
        stu = Students.objects.get(stu_id=u_id)
        com = Competitions.objects.get(com_name=join_name)
        stu.cho_com.add(com)
        return redirect('/consult/')



# 查询学生已经报名的比赛
def consult(request):
    if request.method == 'GET':
        LIST = []
        u_id = request.session.get('id')
        stu = Students.objects.get(stu_id=u_id)
        k = stu.cho_com.all()
        print(k)
        for i in k:
            print(i)
            LIST.append(i)
        return render(request, 'consult.html', {'consult_list': LIST})
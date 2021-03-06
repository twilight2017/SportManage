from django.shortcuts import render
from .models import Students, Admins, Competitions, Notices
from django.shortcuts import render, redirect
from django.contrib.auth import login as LOGIN
from django.contrib.auth import logout as LOGOUT
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.db import transaction
import os
from django.shortcuts import HttpResponse
import xlwt
from io import BytesIO
import qrcode
import xlrd
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
    # 展示已经发布的所有赛事公告信息
    k = Notices.objects.filter()
    LIST = []
    for i in k:
        LIST.append(i)
    return render(request, 'home.html', {'name': _name, 'id': _id, 'notice_list': LIST})


# Admin Home Page
def admhome(request):
    _name = request.session.get('name')
    _id = request.session.get('id')
    # 展示已经发布的所有赛事公告信息
    k = Notices.objects.filter()
    LIST = []
    for i in k:
        LIST.append(i)
    up_name = _name[1:]
    return render(request, 'admhome.html', {'adname': up_name, 'notice_list': LIST})


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
     if request.method == 'GET' or request.method == 'POST':
         LIST = []  # 用于获取后端所有竞赛信息的列表
         k = Competitions.objects.order_by('-com_startime')
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
    if request.method == 'GET':
        k = Competitions.objects.order_by('-com_startime')
        for i in k:
            LIST.append(i)
        LIST1 = []
        u_id = request.session.get('id')
        stu = Students.objects.get(stu_id=u_id)
        k1 = stu.cho_com.all()
        for j in k1:
            LIST1.append(j)
        return render(request, 'choice.html', {'choice_list': LIST, 'alread_list': LIST1})


#  学生加入一个比赛
def join(request, join_name):
        u_id = request.session.get('id')
        stu = Students.objects.get(stu_id=u_id)
        com = Competitions.objects.get(com_name=join_name)
        com.com_total = str(int(com.com_total)+1)
        # 非常重要，改了数据库类的属性值之后一定要进行save操作
        com.save()
        stu.cho_com.add(com)
        url = "http://note.youdao.com/noteshare?id=10f7b9df46bdfe4d94d7c80a993a3d5c"
        img = qrcode.make(url)
        buf = BytesIO()
        img.save(buf)
        image_stream = buf.getvalue()
        response = HttpResponse(image_stream, content_type="image/jpg")
        return response


# 查询学生已经报名的比赛
def consult(request):
    if request.method == 'GET':
        LIST = []
        u_id = request.session.get('id')
        stu = Students.objects.get(stu_id=u_id)
        k = stu.cho_com.all()
        for i in k:
            LIST.append(i)
        return render(request, 'consult.html', {'consult_list': LIST})


# 供管理员进入赛程展示页面
def admpeople(request):
    if request.method == 'GET':
        LIST = []
        k = Competitions.objects.filter()
        for i in k:
            LIST.append(i)
        return render(request, 'admpeopel.html', {'people_list': LIST})


# 用于管理员看到选择了该比赛的人，是多对多关系的反向应用
def admgroup(request, man_name):
    if request.method == 'GET' or request.method == 'POST':
        LIST = []
        com = Competitions.objects.get(com_name=man_name)
        k = com.com_stu.all()
        for i in k:
            LIST.append(i)
        return render(request, 'admgroup.html', {'group_list': LIST, 'com': com})


# 成绩管理页面对所有已发布赛事进行展示
def admmark(request):
    if request.method == 'GET' or request.method == 'POST':
        LIST = []
        k =Competitions.objects.filter()
        for i in k:
            LIST.append(i)
        return render(request, 'admmark.html', {'mark_list': LIST})


# 学生端的成绩查询页面，查看所参加赛事的已发布成绩
def mark(request):
    if request.method == 'GET':
        LIST = []
        u_id = request.session.get('id')  # 获取登录的学生id
        stu = Students.objects.get(stu_id=u_id)  # 根据u_id获取学生对象
        k = stu.cho_com.all()
        for i in k:
            LIST.append(i)
        return render(request, 'mark.html', {'mark_list': LIST})


# 管理员上传当前比赛的成绩信息
def upload(request, ma_name):
    if request.method == 'GET' or request.method == 'POST':
        com = Competitions.objects.get(com_name=ma_name)
        myfile= request.FILES.get("upfile", None)
        com.com_mark = myfile.name
        com.save()
        destination = open(os.path.join("D:\study\soft_project\course_design\com_manage\SportManage\competition\Files", myfile.name), 'wb+')
        # write
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()
        return redirect('/admmark/')


# 实现学生的文件下载功能
def download(request, file_name):
    file = open('Files/'+file_name, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;'
    return response


# 管理员上传当前比赛的成绩信息
def groupup(request, infor_name):
    if request.method == 'GET' or request.method == 'POST':
        com = Competitions.objects.get(com_name=infor_name)
        myfile= request.FILES.get("groupfile", None)
        com.com_infor = myfile.name
        com.save()
        destination = open(os.path.join("D:\study\soft_project\course_design\com_manage\SportManage\competition\Files", myfile.name), 'wb+')
        # write
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()
        return redirect('/admpeople/')


# 生成赛程信息
def create_info(request, export_name):
    # 获取分组数目
    g_number = request.POST.get('GroupNumber')
    g_place = request.POST.get('complace')
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=赛程信息.xls'
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('order-sheet')

    # 设置文件头的样式
    style_heading = xlwt.easyxf()

    # 写入文件信息
    sheet.write(0, 0, '组号')
    sheet.write(0, 1, '学号')
    sheet.write(0, 2, '姓名')
    sheet.write(0, 3, '性别')
    sheet.write(0, 4, '学院')
    sheet.write(0, 5, '比赛地点')
    sheet.write(0, 6, '比赛日期')
    sheet.write(0, 7, '参赛编号')

    com = Competitions.objects.get(com_name=export_name)
    stu = com.com_stu.all()  # 参与了该比赛的所有学生对象
    s_number = com.com_stu.count()  # 参与了该比赛的学生数
    # 按分组信息定义每组元素个数
    if s_number % int(g_number) == 0:
        colomn = s_number // int(g_number)
    else:
        colomn = s_number // int(g_number) + 1
    print(colomn)
    i = 0
    group=1
    while i < s_number:
        j = 1  # 内层循环的循环初始变量
        while j <= colomn and i+j <= s_number:
            sheet.write(i+j, 0, group)
            j = j + 1
        i = i + colomn
        group = group+1

    # 写数据库信息
    data_row = 1
    for k in stu:
        sheet.write(data_row, 1, k.stu_id)
        sheet.write(data_row, 2, k.stu_name)
        if k.stu_gender == '0':
            gender = '男'
        else:
            gender = '女'
        sheet.write(data_row, 3, gender)
        if k.stu_college == '0':
            college = '土木与环境工程学院'
        elif k.stu_college == '1':
            college = '材料科学与工程学院'
        elif k.stu_college == '2':
            college = '机械工程学院'
        elif k.stu_college == '3':
            college = '计算机与通信工程学院'
        elif k.stu_college == '4':
            college = '自动化学院'
        elif k.stu_college == '5':
            college = '数理学院'
        elif k.stu_college == '6':
            college = '化学与生物工程学院'
        elif k.stu_college == '7':
            college = '东凌经济管理学院'
        elif k.stu_college == '8':
            college = '文法学院'
        elif k.stu_college == '9':
            college = '外国语学院'
        elif k.stu_college == '10':
            college = '马克思主义学院'
        sheet.write(data_row, 4, college)
        sheet.write(data_row, 5, g_place)
        dis = request.POST.get('distinct')
        if dis == '0':
            sheet.write(data_row, 6, com.com_startime)
        else:
            sheet.write(data_row, 6, com.com_endtime)
        _id = k.stu_id[4:]
        sheet.write(data_row, 7, _id)
        data_row = data_row + 1

    # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位
    output.seek(0)
    response.write(output.getvalue())
    return response


# 用于上传公告信息
def upnotice(request, distinct_n):
    if request.method == 'GET' or request.method == 'POST':
        k = Notices()  # 新建一个公告对象
        myfile = request.FILES.get("gongao", None)
        k.noti_name = myfile.name
        k.save()
        print(k.noti_name)
        destination = open(
            os.path.join("D:\study\soft_project\course_design\com_manage\SportManage\competition\Files", myfile.name),
            'wb+')
        # write
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()
        return redirect('/admhome/')


# 赋予管理员删除已发布公告的权力
def nodelete(request, del_name):
    Notices.objects.filter(noti_name=del_name).delete()
    return redirect('/admhome/')


# 支持管理员通过excel表格大批量导入比赛
def upcom(request, dis_name):
    if request.method == 'POST' or request.method == 'GET':
        excel_file = request.FILES.get('excel_file', '')
        # 拿到文件后缀
        file_type = excel_file.name.split('.')[1]
        # 仅支持.xlsx、.xls两种格式的文件后缀
        if file_type in ['xlsx', 'xls']:
            # open work file
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            tables = data.sheets()  # 获取每个工作表
            # 循环每个数据表中的数据并写入数据库
            for table in tables:
                rows = table.nrows  # 总行数
                try:
                    # 控制数据库事务交易
                    with transaction.atomic():
                        for row in range(1, rows):
                            row_values = table.row_values(row)
                            co = Competitions()
                            co.com_name = row_values[0]
                            co.com_startime = row_values[1]
                            co.com_endtime = row_values[2]
                            co.com_type = row_values[3]
                            co.com_college = row_values[4]
                            co.save()
                        return redirect('/admdeliver/')
                except:
                    return redirect('/admdeliver/')
        return redirect('/admdeliver/')


def admdesign(request, man_name):
    if request.method == 'GET' or request.method == 'POST':
        LIST = []
        com = Competitions.objects.get(com_name=man_name)
        k = com.com_stu.all()
        for i in k:
            LIST.append(i)
        return render(request, 'admdesign.html', {'group_list': LIST, 'com': com})


# 支持管理员批量导入报名当前比赛的人员名单
def upstu(request, export_name):
    if request.method == 'POST' or request.method == 'GET':
        excel_file = request.FILES.get('stu_file', '')
        # 拿到文件后缀
        file_type = excel_file.name.split('.')[1]
        # 仅支持.xlsx、.xls两种格式的文件后缀
        if file_type in ['xlsx', 'xls']:
            # open work file
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            tables = data.sheets()  # 获取每个工作表
            # 循环每个数据表中的数据并写入数据库
            for table in tables:
                rows = table.nrows  # 总行数
                try:
                    # 控制数据库事务交易
                    with transaction.atomic():
                        for row in range(1, rows):
                            row_values = table.row_values(row)
                            st = Students()
                            st.stu_id = row_values[0]
                            st.stu_name = row_values[1]
                            st.stu_gender = row_values[2]
                            st.stu_college = row_values[3]
                            st.stu_mail = row_values[4]
                            st.stu_password = row_values[5]
                            st.save()
                            com = Competitions.objects.get(com_name=export_name)
                            com.com_total = str(int(com.com_total)+1)
                            com.save()
                            st.cho_com.add(com)
                        return redirect('/admpeople/')
                except:
                    return redirect('/admpeople/')
        return redirect('/admpeole/')
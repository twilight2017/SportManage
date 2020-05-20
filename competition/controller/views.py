from django.shortcuts import render
from .models import Students, Admins

# Create your views here.


def register(request):
    result = ''
    if request.method == "POST" and request.POST:
        # 判断是否为POST请求
        #i_identity = request.POST.get('identity')
        #if i_identity == "参赛人员":
            u_id = request.POST.get('stu_id')
            u_name = request.POST.get('stu_name')
            u_gender = request.POST.get('stu_gender')
            u_college = request.POST.get('stu_college')
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
                    info = Students()
                    info.stu_id = u_id
                    info.stu_name = u_name
                    info.gender = u_gender
                    # info.identity = i_identity
                    info.stu_college = u_college
                    info.stu_mail = u_mail
                    info.stu_password = u_password
                    info.save()
                    result = 'success'
                    return render(request, 'register.html', {'result': result})
            else:
                result = 'error'
                return render(request, 'register.html', {'result': result})
    return render(request, 'register.html', {'result': result})

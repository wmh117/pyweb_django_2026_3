from django.shortcuts import render, HttpResponse, redirect
from app01.models import Department, UserInfo
def index(request):
    return HttpResponse("hello你好bro")


def user_add(request):
    if request.method == "GET":
        return render(request,"user_add.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")
        UserInfo.objects.create(name=user,password=pwd,age=age)
        return redirect("/userlist")

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id = nid).delete()
    return redirect('/userlist')


def orm(request):
    # Department.objects.create(title="销售部")
    # UserInfo.objects.create(name = 'jkm',password = '123',age = 22)
    # UserInfo.objects.create(name='jz', password='1223', age=21)
    # UserInfo.objects.create(name='cz', password='12333', age=12)
    # UserInfo.objects.filter(id = 1).delete()
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.name,obj.password)
    return HttpResponse("ok load the data，，")
def user_list(request):
    data = UserInfo.objects.all()
    print(data)
    return render(request,"user_list.html",{"data":data})
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello你好bro")
def user_list(request):
    #默认去app目录找templates->user_list.html
    return render(request,"user_list.html")
def user_add(request):
    return render(request,"user_add.html")
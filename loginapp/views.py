from django.shortcuts import render,HttpResponse,redirect,render_to_response
from loginapp.models import User
import random,string,os
from loginapp.captcha.image import ImageCaptcha


def registlogic(request):
    namne=request.POST.get("username")
    pwd1=request.POST.get("userpwd1")
    pwd2=request.POST.get("userpwd2")
    u=User.objects.filter(name=namne)
    if not u and pwd1==pwd2:
        User.objects.create(name=namne,password=pwd1)
        return HttpResponse("ok")
    return HttpResponse("error")

# def login(request):
#     name=request.COOKIES.get("name")
#     pwd=request.COOKIES.get("pwd")
#     u1 = User.objects.filter(name=name, password=pwd)
#     if u1:
#         request.session["login"] ="ok"
#         return redirect("emp:emplist")
#     return render(request, "../static/loginapp/../static/login.html")
def loginlogic(request):
    name = request.POST.get("username")
    pwd = request.POST.get("userpwd")
    p=request.GET.get("url")
    u = User.objects.filter(name=name,password=pwd)
    print(p)
    if u:
        r1=redirect("emp:emplist")
        r1.set_cookie("name",name,max_age=7*24*3600)
        r1.set_cookie("pwd",pwd,max_age=7*24*3600)
        request.session["login"]="ok"
        return HttpResponse("ok")
    return HttpResponse("error")


def getcap(request):
    image=ImageCaptcha()
    code=random.sample(string.ascii_letters+string.digits,4)
    code = "".join(code)
    print(code)
    request.session["code"]=code
    data=image.generate(code)
    return HttpResponse(data,"image/png")
def checkname(request):
    name=request.POST.get("username")
    u=User.objects.filter(name=name)
    if u:
        return HttpResponse("error")
    return HttpResponse("ok")


def checkcaptcha(request):
    cap=request.POST.get('cap')
    print(cap)
    if cap.lower()==request.session['code'].lower():
        return HttpResponse("ok")
    return HttpResponse("error")
# Create your views here.

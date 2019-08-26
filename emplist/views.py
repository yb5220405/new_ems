from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from emplist.models import Emp
import os,uuid

def emplist(request):
    def default(ems):
        if isinstance(ems, Emp):
            return {'id': ems.id, 'name': ems.name, 'age': ems.age, 'salary': str(ems.salary), 'headpic': str(ems.headpci)}
    emslist = list(Emp.objects.all())
    return JsonResponse({'ems': emslist}, safe=False, json_dumps_params={'default':default})


def addlogic(request):
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    age=request.POST.get("age")
    head=request.FILES.get("headpic")
    head.name=str(uuid.uuid4())+os.path.splitext(head.name)[1]
    emp1=Emp.objects.create(name=name,age=age,salary=salary,headpci=head)
    if emp1:
        # page=pages.page(pages.num_pages)
        return HttpResponse("ok")
    return HttpResponse("error")


def delete(request):
    id = request.GET.get("id")
    print(id)
    emp = Emp.objects.get(id=id)
    if emp:
        emp.delete()
        return HttpResponse(1)

def update(request):
    id = request.GET.get("id")
    print(id)
    ems = Emp.objects.get(id=id)
    if ems:
        request.session["updateId"] = id
        return HttpResponse(1)
    return HttpResponse(0)



def loadupdate(request):
    def default(ems):
        if isinstance(ems, Emp):
            return {'id': ems.id, 'name': ems.name, 'age': ems.age, 'salary': str(ems.salary), 'headpic': str(ems.headpci)}
    param = request.GET.get("param")
    id = request.session.get(param)
    ems = Emp.objects.get(id=id)
    return JsonResponse({'eu':ems},safe=False,json_dumps_params={'default':default})


def updatestatus(request):
    try:
        with transaction.atomic():
            id = request.POST.get("eId")
            ems = Emp.objects.get(id=id)
            ems.name = request.POST.get("name")
            ems.salary = request.POST.get("salary")
            ems.age = request.POST.get("age")
            headpic = request.FILES.get("headpic")
            if headpic:
                ext = os.path.splitext(headpic.name)
                headpic.name = str(uuid.uuid4()) + ext[1]
                ems.headpic = headpic
            ems.save()
            return  HttpResponse(1)
    except:
        return HttpResponse(0)

def login(request):
    s=request.session.get("login")
    if s:
        return HttpResponse("ok")
    return HttpResponse("error")





# Create your views here.

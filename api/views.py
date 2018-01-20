from django.shortcuts import render, HttpResponse
import datetime
from api import models


# Create your views here.

def cur_time(request):
    time = datetime.datetime.now()
    return render(request, 'cur_time.html', {"time": time})


def userInfo(request):
    # name=[]

    if (request.method == "POST"):
        name = request.POST.get("username", None)
        sex1 = request.POST.get("sex", None)
        email1 = request.POST.get("username", None)
        models.UserInfo.objects.create(
            username=name,
            sex=sex1,
            email=email1
        )
        lists = models.UserInfo.objects.all()
        return render(request, 'index.html', {"name": lists})
    lists = models.UserInfo.objects.all()
    print(list(lists))
    return render(request, 'index.html', {"name": lists})

def sp_2003(request,num,nums):

    return  HttpResponse(num,nums)

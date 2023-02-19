# from django.http import HttpResponse
from django.shortcuts import render

from . models import Place,Team

# Create your views here.
def home(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
# def addition(request):
#     a=int(request.GET['n1'])
#     b=int(request.GET['n2'])
#     res=a+b
#     subt=a-b
#     mult=a*b
#     divi=a//b
#     return render(request,"result.html",{'ad':res,'sub':subt,'mul':mult
#                         ,'div':divi})

def about(request):
    return render(request,"about.html")
# def contact(request):
#     return HttpResponse("this is contactpage")
# def detail(request):
#     return render(request,"detail.html")
# def thanx(request):
#     return HttpResponse("this is thanksgivingpage")

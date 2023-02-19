from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method =='POST':
        u1=request.POST['username']
        f1=request.POST['first_name']
        l1=request.POST['last_name']
        e1=request.POST['email']
        p1=request.POST['password']
        c1=request.POST['cpassword']
        if p1==c1:
            if User.objects.filter(username=u1).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=e1).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=u1, first_name=f1,
                                                last_name=l1, email=e1,password=p1)
                user.save();
                return redirect('login')
            print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
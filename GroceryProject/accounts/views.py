from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User,auth
from . import models

# Create your views here.
def login(request):
    #print('login')
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        userMaster = models.UserMaster.objects.filter(email=email).first()
        #print(userMaster)
        if userMaster is not None:
            print(userMaster)
            user=auth.authenticate(username=userMaster.username,password=password)
            if user is not None:
                print('true')
                auth.login(request,user)
                return redirect("products:productList")
            else:
                print('false')
                messages.info(request,'invalid credentials')
                return redirect('accounts:login')
        else:
            print('false')
            messages.info(request,'user not found')
            return redirect('accounts:login')
    else:
        return render(request,'login.html')
    
def register(request):
    if request.method=="POST":
        print(request.POST)
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        emailid=request.POST['email']
        password=request.POST['password']
        user=models.UserMaster.objects.create_user(username=emailid,first_name=firstname, last_name=lastname, email=emailid,password=password)
        auth.login(request,user)
        return redirect("products:productList")
    else:
        return render(request,"register.html")
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('accounts:login')
    else:
        return HttpResponse('<b>user is not logged in</b>')
    

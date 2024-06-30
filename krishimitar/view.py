from django.http import HttpResponse,HttpRequest ,HttpResponseRedirect
from math import e
from django.shortcuts import render,redirect
from Service.models import Service
from django.core.paginator import Paginator
from sell.models import Sell
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .settings import *
from django.core.mail import send_mail
from django import forms
from Bima.models import Bima

def home(request):
    servicedata=Service.objects.all()
    data={
        "servicedata":servicedata,
        "title":"home"
        }
    
    return render(request,"home.html",data)

def signin(request):
    if request.method == "POST":
        name=request.POST.get('name')
        passwd=request.POST.get('password')
        
        user=authenticate(request,username=name,password=passwd)
        if user:
            login(request,user)
            return render(request,"home.html",{"title":"login","name":name})
        else:
            messages.error(request,"Bad Credentials") 
            return redirect('home')       
    data={"title":"login"}
    return render(request,"login.html",data)

def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        passwd=request.POST['password']
        check=False
        if 'check' in request.POST:
            check=True
        
        if User.objects.filter(username=name):
            messages.error(request,"Username already exists")
            return redirect("home")
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
            return redirect("home")
            
        if len(name)>10:
            messages.error(request,"Username length should be less than 10")
            return redirect("home")
        
        if not name.isalnum():
            messages.error(request,"Username must be alpha numeric")
            return redirect("home")
        
        
        subject="Welcome to our website Krishimitar .Thank you for regestering.This is for your service.Hope you enjoy our services and like it .Please confirm your email address in order to activvate your account"
        message="Hello"+name+"\n"
        
        from_email=EMAIL_HOST_USER
        to_list=[email]
        # if send_mail(subject,message,from_email,to_list):
        #     print("hii")
        # else:
        #     print("hello")
        
        myuser=User.objects.create_user(name,email,passwd)
        if check:
            user=authenticate(request,username=name,password=passwd)
            messages.success(request,"Account has been created successfully")
            login(request,user)
            return render(request,"home.html")
    
    data={"title":"signup"}
    return render(request,"sign_up.html",data)

def sell(request):
    selldata=Sell.objects.all().filter(user_name=request.user)
    data={"title":"sell",'selldata':selldata}
    return render(request,"sell.html",data)


def saveSell(request):
    if request.method=="POST":
        item_image=None
        # print(request.user)
        # if not request.user.is_authenticated:
        #     messages.error(request,"User name not registered")
        #     return render(request,"login.html")
        form=Sell(request.POST, request.FILES)
        if form:
            item_image=request.FILES["item_image"]
        else:
            form=Sell()
        
        u_name=request.user
        name=request.POST.get("item_name")
        detail=request.POST.get("item_details")
        date=request.POST.get("item_date")
        quantity=request.POST.get("item_quantity")
        price=request.POST.get("item_price")
        d=Sell(item_img=item_image,user_name=u_name,item_title=name,item_detail=detail,item_date=date,item_quant=quantity,item_price=price)
        d.save()
        messages.success(request,"Registered Successfully")
       
        
    selldata=Sell.objects.all().filter(user_name=request.user)
    data={"title":"sell",'selldata':selldata}
    return render(request,"sell.html",data)


def buy(request):
    if request.user.is_authenticated:
        buydata=Sell.objects.all().exclude(user_name=request.user)
        data={"title":"buy",'buydata':buydata}
        return render(request,"buy.html",data)
    buydata=Sell.objects.all()
    data={"title":"buy",'buydata':buydata}
    return render(request,"buy.html",data)

def bima(request):
    if request.user.is_authenticated:
        d=Bima.objects.all().filter(user_name=request.user)
        data={"title":"bima",'data':d}
        return render(request,"bima.html",data)
    return render(request,"bima.html",{"title":"bima"})

def signout(request):
    logout(request)
    
    messages.success(request,"Logged Out Successfully")
    return redirect('home')

def saveBima(request):
    if request.method=="POST":
        u_name=request.POST.get("farmer_name")
        size=request.POST.get("land_size")
        rno=request.POST.get("rakba_no")
        inc=request.POST.get("annual_income")
        tpe=request.POST.get("crop_type")
        name=request.POST.get("crop_name")
        if Bima.objects.all().filter(rno=rno):
            messages.error(request,"Rakba no already exists")
            return redirect('saveBima')
        d=Bima(user_name=u_name,size=size,rno=rno,income=inc,type=tpe,cropname=name)
        d.save()
        messages.success(request,"Registered Successfully")
       
        
    dt=Bima.objects.all().filter(user_name=request.user)
    data={"title":"bima",'data':dt}
    return render(request,"bima.html",data)

def chatting(request):
    return render(request,'chat.html')

def buysell(request):
    image=request.GET.get('images')
    title=request.GET.get('title')
    detail=request.GET.get('details')
    quan=request.GET.get('quantity')
    price=request.GET.get('price')
    date=request.GET.get('date')
    b=Sell.objects.all().filter(item_title=title,item_detail=detail,item_quant=quan,item_price=price)
    name=b[0].user_name
    
    context={
        'name':name,
        'image':image,
        'title':title,
        'detail':detail,
        'quantity':quan,
        'price':price,
        'date':date,
        }  
    return render(request,"buysell.html",context)

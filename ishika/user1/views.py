from django.shortcuts import render,redirect
from django.http import HttpResponse
from user1.models import *

# Create your views here.
def first(request) :
    return HttpResponse("This is my First Webpage")

def login(request) :
    if request.method == "POST":
        email1=request.POST['email']
        password1=request.POST['password']
        data=user1.objects.get(user_email=email1,user_password=password1)
        if data:
                request.session['email']=data.user_email
                
                return redirect('dcb')
        else:
                return render(request,'login2.html',{'message':'Invalid email or password'})
        
    return render(request,'login2.html')

def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('dcb')
    else:
        return redirect('dcb')
def registrationpage(request):
    if request.method == "POST":
        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['password']
        phone1=request.POST['phone']
        pincode1=request.POST['pincode']
       
        print(name1,email1,password1,phone1)
        data=user1(user_name=name1,user_email=email1,user_password=password1,user_contact=phone1,user_pincode=pincode1)
        a=user1.objects.filter(user_email=email1)
        if len(a)==0:
            data.save()
            return redirect('abcd')
        else:
            return render(request,'Registration.html',{'message':"user alredy exist"}) 

    return render(request,'Registration.html') 

    

def tableview(request) :
    a=user1.objects.all()
    print('data',a)
    return render(request,'table.html',{"data":a})

def tablefilter(request) :
    a=user1.objects.filter(user_email='ishikamakhija.7@gmail.com')
    print('data',a)
    return render(request,'table.html',{"data":a})

def tableget(request) :
    a=user1.objects.get(user_email='ishikamakhija.7@gmail.com')
    print('data',a)
    return render(request,'table_get.html',{"data":a})

def producttable(request):
    b=Product.objects.all()
    print('data',b)
    return render(request,'table2.html',{"data":b})

def producttable_filter(request):
    b=Product.objects.filter(name='jeans')
    print('data',b)
    return render(request,'table2.html',{"data":b}) 

def producttable_get(request):
    b=Product.objects.get(price=5000)
    print('data',b)
    return render(request,'product_get.html',{"data":b})  

def index(request) :
        if 'email' in request.session:
            a=request.session['email']
            data=Category.objects.all()
            return render(request,'base.html',{'data':data,'a':a})
        else:
            data=Category.objects.all()
            return render(request,'base.html',{'data':data})
   
def contact(request) :
    return render(request,'contact.html')
def about(request) :
    return render(request,'about.html')

def product_display(request) :
    data=Category.objects.all()
    return render(request,'product.html',{'data':data})

def product_display_all(request) :
    data=Product.objects.all()
    return render(request,'product_display.html',{'data':data})

def productcategorywise(request,id) :
    data=Product.objects.filter(category=id)
    return render(request,'product_display.html',{'data':data})


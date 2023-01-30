from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from N_Shop.form import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)

def placeOrder(request,i):
    customer= Customer.objects.get(id=i)
    if(request.method=='POST'):
        form=Createorderform(request.POST,instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'placeorder.html',context)


def addProduct(request):
    form=Createproductform()
    if(request.method=='POST'):
        form=Createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'addProduct.html',context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=Createuserform()
        customerform=Createcustomerform()
        if request.method=='POST':
            form=Createuserform(request.POST)
            customerform=Createcustomerform(request.POST)
            if form.is_valid() and customerform.is_valid():
                user=form.save()
                customer=customerform.save(commit=False)
                customer.user=user 
                customer.save()
                return redirect('login')
        context={
            'form':form,
            'customerform':customerform,
        }
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')


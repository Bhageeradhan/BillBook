from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def LoginPage(request):
    if request.user.is_authenticated :
        return redirect('/inventory/producttable/')
    
    context = {
        "error":""
    }
    
    if request.method =="POST":
        print(request.POST)
        
        user = authenticate(username=request.POST['username'] , password=request.POST['password'])
        
        print(user.role)
        
        if user is not None:
            
            login(request,user)
            return redirect('/ordermanagement/customertable/')
        else:
            context = {
                "error":'*Invalid Username or Password'
            }
            return render(request,'login.html',context)
    return render(request,'login.html',context)

def Logout(request):
    
    logout(request)
    
    return redirect('/')

def Signin(request):
    context={
        'error':''
    }
    
    if request.method == 'POST':
        
        check_user = User.objects.filter(username=request.POST['username'])
        
        if len(check_user) > 0:
            
            context={
                'error':'*Username already exist'
            }
            
            return render(request,'signup_form.html',context)
        
        else:
            
            new_user = User(username=request.POST['username'], password=request.POST['password'], first_name=request.POST['firstname'],
                        last_name = request.POST['lastname'], email=request.POST['emailaddress'], age = request.POST['age'])
        
            new_user.set_password(request.POST['password'])
        
            new_user.save()
            
            return redirect('/')
            
    return render(request,'signup_form.html',context)
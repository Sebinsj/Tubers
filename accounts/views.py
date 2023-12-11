from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method=='POST':
        user_name=request.POST["user_name"]
        password=request.POST["password"]

        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('login')    

    return render(request,'accounts/login.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        user_name=request.POST["user_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        
        if password==confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.warning(request,'username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'email exits')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=user_name,email=email,password=password,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'Account Created Successfully!')
                    return redirect('login')
        
        else:
            messages.warning(request,'passwords do not match')
            return redirect('register')

    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')


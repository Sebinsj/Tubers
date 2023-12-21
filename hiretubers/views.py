from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages
# Create your views here.
def hiretuber(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        tuber_id=request.POST['tuber_id']
        tuber_name=request.POST['tuber_name']
        email=request.POST['email']
        city=request.POST['city']
        phone=request.POST['phone']
        state=request.POST['state']
        message=request.POST['message']
        user_id=request.POST['user_id']
    
    #santitization    

    hiretuber=Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,email=email,city=city,phone=phone,state=state,message=message,user_id=user_id)

    hiretuber.save()
    messages.success(request,'thanks for reaching out')
    return redirect('youtubers')

def home(request):
    return render(request,'webpages/home.html')

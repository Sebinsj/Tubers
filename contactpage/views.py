from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.

def contact(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        phone=request.POST['phone']
        email=request.POST['email']
        company=request.POST['company']
        subject=request.POST['subject']
        message=request.POST['message']
        user_id=request.POST['user_id']
    
    #santitization    

    contact=Contact(fullname=fullname,phone=phone,email=email,company=company,subject=subject,message=message,user_id=user_id)

    contact.save()
    messages.success(request,'thanks for reaching out')
    return redirect('contact')




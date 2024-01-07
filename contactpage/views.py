from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.

def contact(request):
    if request.method=='POST':
        fname=request.POST['fname']
        phone=request.POST['phone']
        email=request.POST['email']
        company=request.POST['company']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(fname=fname,phone=phone,email=email,company=company,subject=subject,message=message)

        contact.save()
        messages.success(request,'thanks for reaching out')
        
    
       

    messages.success(request,'thanks for reaching out')
    return redirect('home')




from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
from django.contrib import messages
from contactpage.models import Contact

# Create your views here.
def home(request):
    sliders=Slider.objects.all()
    teams=Team.objects.all()
    featured_youtubers=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers=Youtuber.objects.order_by('-created_date')
    data={
        'sliders':sliders,
        'teams':teams,
        "featured_youtubers":featured_youtubers,
        'all_tubers':all_tubers,
    }
    return render(request,'webpages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'webpages/about.html',data)
      
def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    if request.method=='POST':
        print(request.POST)
        fname=request.POST['fname']
        phone=request.POST['phone']
        email=request.POST['email']
        company=request.POST['company']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(fname=fname,phone=phone,email=email,company=company,subject=subject,message=message)
        contact.save()
        messages.success(request,'thanks for reaching out')    # return None
    return render(request,'webpages/contact.html')

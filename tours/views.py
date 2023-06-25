from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import location
from  location.models import Add_location,Book_location,Guide
from .models import *

# Create your views here.
def landing(request):
    data = Add_location.objects.all()
    return render(request,'landing.html',{'title':'Tours & Travels','data':data})
    
def home(request):
    data = Add_location.objects.all()
    return render(request,'index.html',{'title':'Home','data':data})

def about(request):
    return render(request,'about.html',{'title':'About'})

def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            contact = ContactUs.objects.create(name=name,email=email,message=message)
            contact.save()
            messages.success(request,"You will be contacted soon")

    except ValueError:
        messages.error(request,'Error')

    return render(request,'contact.html',{'title':'Contact us'})
    
@login_required(login_url="/accounts/login")
def details(request,p_id):
    try:
        if request.method == 'POST':
            pnames = request.POST['pname']
            guide = request.POST['guide']
            people = request.POST['people']
            sdate = request.POST['sdate']
            edate = request.POST['edate']
            edata = Book_location.objects.create(pname=pnames,guide=guide.set(),people=people,sdate=sdate,edate=edate)
            edata.save()
            messages.success(request,'booked successfully')
    except ValueError:
        messages.error(request,'error')
    data = Add_location.objects.get(id=p_id)
    gdata = Guide.objects.all()
    return render(request,'details/details.html',{'data':data,'guide':gdata})

def search(request):
    if request.method == 'POST':
        searchs = request.POST['search']
        sname = Add_location.objects.filter(name__contains=searchs)
        return render(request,'search.html',{'title':searchs,'search':sname,'searchs':searchs})
    
    else:
        return render(request,'search.html')
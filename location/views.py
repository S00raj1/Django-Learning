from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def admin_view(request):
    return render(request,"admin/admin.html",{'title':'Home'})


@csrf_exempt
def add(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            location = request.POST['location']
            description = request.POST['description']
            images = request.FILES['image']
            price = request.POST['price']
            add_data = Add_location.objects.create(name=name,location=location,description=description,image=images,price=price)
            add_data.save()
            messages.success(request,'Location uploaded succesfully')
    except ValueError:
        messages.error(request,'Location couldnot be uploaded')
    return render(request,'admin/add.html',{'title':'Add location'})


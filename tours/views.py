from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html',{'title':'Home'})

def about(request):
    return render(request,'about.html',{'title':'About'})

def contact(request):
    return render(request,'contact.html',{'title':'Contact us'})
    
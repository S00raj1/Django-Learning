from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User,auth

# Create your views here.


def user_login(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request,username=username,password=password)
    # if user is not None:
    #     login(request,user)
    #     return redirect(request,'/')
    return render(request,'./login/login.html',{'title':'login'})

def user_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        data = User.objects.create_user(fname=fname,lname=lname,username=username,email=email,password=password)
        data.save()
    return render(request,'./login/signup.html',{'title':'signup'})

def user_logout(request):
    logout(request)
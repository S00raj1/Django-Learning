from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('/location/admin-view')
            login(request,user)
            return redirect('/home')
        messages.error(request, 'Incorrect username or password')
        
    return render(request,'./login/login.html',{'title':'login'})

def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            data = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            data.save()
            return redirect('/accounts/login')
        messages.error(request,"Your password doesnot match")
        
    return render(request,'./login/signup.html',{'title':'signup'})

def user_logout(request):
    logout(request) 
    return redirect("/accounts/login")
    
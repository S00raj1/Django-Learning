from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateUserForm,UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

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
    
@login_required(login_url="/accounts/login")
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"your profile is updated successfully")
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request,'profile/profile.html',{'title':'Profile', 'user_form':user_form,'profile_form':profile_form})
    




class ChangePasswordView(SuccessMessageMixin,PasswordChangeView):
    template_name = 'login/changepassword.html'
    success_message = "Successfully Changed Your Password"
    title = 'Change Password'
    success_url = reverse_lazy('home')
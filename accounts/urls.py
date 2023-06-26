from django.urls import path
from . import views
from .views import ChangePasswordView

urlpatterns = [
    path('login/',views.user_login, name ='login'),
    path('signup/',views.user_signup),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile,name='profile'),
    path('password-change/',ChangePasswordView.as_view(),name='password-change'),
]
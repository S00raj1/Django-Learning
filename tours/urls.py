from django.urls import path
from . import views

urlpatterns = [
    path("",views.landing),
    path("home/",views.home,name = 'home'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('details/<int:p_id>', views.details, name= 'details'),
    path('search',views.search,name='search'),
]
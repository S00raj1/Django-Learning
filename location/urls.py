from django.urls import path 
from . import views

urlpatterns=[
    path('admin-view',views.admin_view),
    path('add',views.add)
]
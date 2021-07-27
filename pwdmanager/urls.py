from django.urls import path, include
from django.contrib.auth.decorators import login_required

from pwdmanager import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', 
         login_required(views.PwdCreateView.as_view(
             template_name="pwdmanager/pwd.html"
         )),
         name="add"),
    path('view/<str:pk>', views.view, name="view"),
]

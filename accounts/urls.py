from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.account, name="account"),
    path('register', views.register, name="register"),
]

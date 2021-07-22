from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from .forms import UserRegisterForm
from .models import User


@login_required
def account(request):
    messages.success(request, "Login successful!")
    context = {
        'user': request.user,
        'confirmed': False,
    }

    return render(request, "accounts/account.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please login.")
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }

    return render(request, 'accounts/register.html', context)

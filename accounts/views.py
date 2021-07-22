from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm


def account(request):
    if request.method == "POST":
        pass
    return


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }

    return render(request, 'accounts/register.html', context)

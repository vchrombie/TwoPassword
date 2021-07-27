from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.views.generic import CreateView

from .crypter import encrypt, decrypt

from .models import Pwd


@login_required
def home(request):
    user = request.user
    pwd = Pwd.objects.filter(author=user)
    context = {
        'pwd': pwd
    }
    return render(request, "pwdmanager/home.html", context)


class PwdCreateView(CreateView):
    model = Pwd
    fields = [
        'website_name',
        'website_link',
        'website_username',
        'website_password',
        'website_notes',
    ]

    def form_valid(self, form):
        if form.is_valid():
            user = self.request.user
            form.instance.author = user

            website_password = form.instance.website_password
            form.instance.website_password = encrypt(website_password)

            super().form_valid(form)
            messages.success(self.request, "Password saved!")

            return redirect('home')

        else:
            messages.error(self.request, "Error")


@login_required(login_url='/accounts/login')
def view(request, pk):
    user = request.user
    pwd = Pwd.objects.get(id=pk, author=user)

    user_master_password = request.user.password

    message = ''

    if request.method == "POST":
        website_password = pwd.website_password
        form_master_password = request.POST.get("master_password")

        if not check_password(form_master_password, user_master_password):
            message = 'Wrong Master Password'

        else:
            if website_password := decrypt(website_password):
                context = {
                    'pwd': pwd,
                    'website_password': website_password,
                    'confirmed': True,
                }

                return render(request, "pwdmanager/view.html", context)

            else:
                message = "Please try again"

    context = {
        'pwd': pwd,
        'message': message,
    }

    return render(request, "pwdmanager/view.html", context)


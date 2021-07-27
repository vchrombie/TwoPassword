from django.db import models
from django.urls import reverse

from accounts.models import User


class Pwd(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    website_name = models.CharField(max_length=28)
    website_link = models.URLField(max_length=56, null=True)
    website_username = models.CharField(max_length=28)
    website_password = models.CharField(max_length=28)
    website_notes = models.CharField(max_length=56, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_name

    def get_absolute_url(self):
        return reverse("account")

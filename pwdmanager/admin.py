from django.contrib import admin

from .models import Pwd

admin.site.site_header = "Admin Dashboard: TwoPassword"


class AdminConfig(admin.ModelAdmin):
    list_display = ('website_name', 'author', 'created')
    exclude = ('website_password', 'master_password')


admin.site.register(Pwd, AdminConfig)

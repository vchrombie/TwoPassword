from django.contrib import admin
from accounts.models import User


class AdminConfig(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'is_staff', 'is_superuser')
    exclude = ('password',)


admin.site.register(User, AdminConfig)

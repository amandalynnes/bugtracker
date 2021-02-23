from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TicketItem
from .forms import CustomUserForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserForm
    model = CustomUser
    list_filter = ['username', 'email',]
    fieldsets = (
        [None, {'fields': ('email', 'username', 'password')}],
    )
    add_fieldsets = (
        [None, {'fields': ('email', 'username', 'password')}],
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TicketItem)

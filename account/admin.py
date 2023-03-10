from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Address

class MyUserManager(UserAdmin):
    model = MyUser

    list_display = ('id', 'username', 'email', 'phone', 'is_active', 'is_staff')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone', 'password')}),
        ('Разрешения', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone', 'is_staff', 'is_active')
        }),
    )


admin.site.register(MyUser, MyUserManager)
admin.site.register(Address)


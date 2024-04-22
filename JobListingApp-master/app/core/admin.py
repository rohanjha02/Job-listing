from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
from django.utils.translation import gettext as _


# Register your models here.

class UserAdmin(BaseUserAdmin):
    """
    1) user name & email & phone number is listed on chage list page
    2)for chage or edit user page we show fields from fieldsets
    3)for add or create user page we show fields from add_fieldsets .
    """
    ordering = ['id']
    list_display = ['email', 'name', 'phone_number']
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email', 'password'
                )

            }

        ),
        (
            _('Personal Info'),
            {
                'fields': ('name', 'phone_number', )
            }
        ),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')

            }
        ),
        (
            _('Important dates'),
            {
                'fields': ('last_login',)
            }

        )
    )

    add_fieldsets = (
        (
            _('Create user profile'),
            {
                'classes': ('wide',),
                'fields': ('name', 'email','phone_number', 'password1', 'password2',)

            }

        ),
    )


admin.site.register(models.User, UserAdmin)

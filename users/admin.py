from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Register your models here.


@admin.register(User)
class MyUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Advanced options",
            {
                "fields": ("company_code",),
            },
        ),
    )

    list_display = ("username", "company_code")

from django.contrib import admin
from outs.models import Out

# Register your models here.


@admin.register(Out)
class OutAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "quantity",
        "owner",
        "created",
        "updated",
    )

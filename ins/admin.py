from django.contrib import admin
from ins.models import In

# Register your models here.


@admin.register(In)
class Indmin(admin.ModelAdmin):

    list_display = (
        "name",
        "quantity",
        "owner",
        "created",
        "updated",
    )

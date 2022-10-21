from django.contrib import admin

from profiles.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "city", "country")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("address", "city", "country")

from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'price', 'duration')  # ✅ valid fields
    search_fields = ('name', 'destination__name')
    list_filter = ('destination',)

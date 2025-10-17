from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'price', 'created_at')  
    search_fields = ('name', 'country')

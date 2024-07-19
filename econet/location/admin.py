from django.contrib import admin
from .models import CollectionBin

@admin.register(CollectionBin)
class CollectionBoxAdmin(admin.ModelAdmin):
    list_display = ('bin_id_number', 'description')
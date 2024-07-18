from django.contrib import admin
from .models import CollectionBin

@admin.register(CollectionBin)
class CollectionBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'location_description')
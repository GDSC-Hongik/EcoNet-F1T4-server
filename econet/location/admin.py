from django.contrib import admin
from .models import CollectionBox

@admin.register(CollectionBox)
class CollectionBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'location_description')
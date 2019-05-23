from django.contrib import admin

# Register your modefrom 
from .models import Album,Song

admin.site.register(Album)
admin.site.register(Song)



from django.contrib import admin
from .models import Trailer

class TrailerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'release', 'like')

admin.site.register(Trailer, TrailerAdmin)

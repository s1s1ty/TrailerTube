from django.contrib import admin
from .models import Trailer, Message


def make_approved(modeladmin, request, queryset):
    queryset.update(approved=True)

class TrailerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'release', 'approved')
    actions = [make_approved]

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(Message, MessageAdmin)

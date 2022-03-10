from django.contrib import admin
from .models import Actor
# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

admin.site.register(Actor,ActorAdmin)

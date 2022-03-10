from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

admin.site.register(Movie,MovieAdmin)
# Register your models here.

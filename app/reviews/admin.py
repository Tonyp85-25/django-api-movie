from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('grade', 'movie')
    list_display_links = ('grade', 'movie')
    search_fields = ('grade', 'movie')

admin.site.register(Review,ReviewAdmin)

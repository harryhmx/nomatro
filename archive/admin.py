from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_author', 'slug', 'hits',)

    def show_author(self, obj):
        try:
            text = obj.author.username
        except:
            text = 'Unknown'
        return text
    show_author.short_description = 'Author'

from django.contrib import admin
from . models import Blogpost


# Registering Blogpost model in admin panel with required fields are id,title and desc.

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

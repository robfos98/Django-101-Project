from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
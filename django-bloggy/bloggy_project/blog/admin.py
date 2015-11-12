from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    """docstring for PostAdmin"""
    list_display=('title','created_at','views')

admin.site.register(Post,PostAdmin)

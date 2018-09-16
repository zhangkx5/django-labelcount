from django.contrib import admin

# Register your models here.
from labelcount.models import BlogsPost


class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']

admin.site.register(BlogsPost, BlogsPostAdmin)
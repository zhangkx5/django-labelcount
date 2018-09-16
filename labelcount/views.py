from django.shortcuts import render

# Create your views here.
from labelcount.models import BlogsPost


def blog_index(request):
    blog_list = BlogsPost.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list})
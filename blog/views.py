from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'estetico/blog.html', context)


def blog_detail(request, slug):
    context = {
        'post': Post.objects.get(slug=slug)
    }
    return render(request, 'estetico/blog_detail.html', context)


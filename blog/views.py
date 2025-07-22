# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
from datetime import datetime

def index(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/index.html', {
        'posts': posts,
        'current_time': datetime.now(),
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', { 'post': post })


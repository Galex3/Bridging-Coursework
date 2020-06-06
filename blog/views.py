from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

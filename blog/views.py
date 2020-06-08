from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

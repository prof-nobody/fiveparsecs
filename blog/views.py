from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:5]


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePost():
    pass

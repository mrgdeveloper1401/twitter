from django.shortcuts import render
from posts.models import Post, Category
from django.views.generic import CreateView, DetailView, DeleteView, ListView


class ListPostView(ListView):
    template_name = 'posts/list_post.html'
    model = Post


class CreatePostView(CreateView):
    pass


class DetailPostView(DetailView):
    template_name = 'posts/details_post.html'
    model = Post


class DeletePostView(DeleteView):
    pass

from django.shortcuts import render
from dhango.views import View
from .models import Post
from .forms import PostForm


class PostListView(View):
    """Lists all posts of current user"""
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'posts/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=Flase)
            new_post.author = request.user # get the current loggedin user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'posts/post_list.html', context)

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


class StartingPageView(ListView):

    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    

def posts(request):
    """View for view all posts list page."""
    all_posts = Post.objects.all().order_by("-date")
    context = {
        "all_posts": all_posts
    }

    return render(request, "blog/all-posts.html",  context)


def post_details(request, slug):
    """View for view all posts list page."""
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post,
        "post_tags": post.tags.all()
    }

    return render(request, "blog/post-detail.html", context)


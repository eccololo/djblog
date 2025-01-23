from django.shortcuts import render, get_object_or_404
from .models import Post


def starting_page(request):
    """View for view all posts list page."""
    latest_posts = Post.objects.all().order_by("-date")[:3]
    context = {
        "posts": latest_posts
    }
    return render(request, "blog/index.html", context)

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


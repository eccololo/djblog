from django.shortcuts import render
from datetime import date
from .models import Post


# Dumy data
all_posts = []


def get_date(post):
    return post['date']

def starting_page(request):
    """View for view all posts list page."""
    latest_posts = Post.objects.all().order_by("-date")[:3]
    context = {
        "posts": latest_posts
    }
    return render(request, "blog/index.html", context)

def posts(request):
    """View for view all posts list page."""

    context = {
        "all_posts": all_posts
    }

    return render(request, "blog/all-posts.html",  context)


def post_details(request, slug):
    """View for view all posts list page."""
    post = next(post for post in all_posts if post["slug"] == slug)
    context = {
        "post": post
    }

    return render(request, "blog/post-detail.html", context)


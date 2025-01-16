from django.shortcuts import render
from django.http import HttpResponse



def starting_page(request):
    """View for view all posts list page."""
    context = {

    }
    return render(request, "blog/index.html", context)

def posts(request):
    """View for view all posts list page."""
    return render(request, "blog/all-posts.html")


def post_details(request, slug):
    """View for view all posts list page."""
    return HttpResponse("Single post page.")


from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    """View for view all posts list page."""
    context = {
        
    }
    return render(request, "index.html", context)

def posts(request):
    """View for view all posts list page."""
    return HttpResponse("ALl posts list.")

from django.shortcuts import render
from datetime import date


# Dumy data
posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Mateusz',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': "There is nothing like the views when hiking in the mountains! And I wasn't even prepared for what happened while I was enjoying the view!",
        'content': """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?
        """
    },
     {
        'slug': 'coding-in-the-skys',
        'image': 'coding.jpg',
        'author': 'Alextrasza',
        'date': date(2023, 5, 18),
        'title': 'Coding My App',
        'excerpt': "I like to code apps and this is how I code a great app that bringed me a lot of money.",
        'content': """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?
        """
    },
     {
        'slug': 'woods-and-trees',
        'image': 'woods.jpg',
        'author': 'Jerry',
        'date': date(2020, 4, 25),
        'title': 'Woods Are Comming to Live',
        'excerpt': "THis is how woods are comming to live after a long winter. I went to see trees in woods and I saw them comming to live",
        'content': """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga placeat
            necessitatibus ipsam deleniti ducimus laborum assumenda. Placeat, mollitia!
            Officiis consequuntur facere tempora nisi quaerat at perspiciatis mollitia
            quia! Architecto, aliquid?
        """
    }
]


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
    return render(request, "blog/post-detail.html")


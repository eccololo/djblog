from django.contrib import admin
from .models import Post, Tag, Author, Comment



class CommentAdmin(admin.ModelAdmin):

    list_display = ["user_name", "post"]

class PostAdmin(admin.ModelAdmin):
    
    list_filter = ["author", "tags", "date"]
    list_display = ["title", "date", "author"]
    prepopulated_fields = { "slug": ("title",) }



admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

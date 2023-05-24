from django.contrib import admin
from .models import Post, Author, Tag, comment
# Register your models here.


class postAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date", )
    list_display =("title","date", "author", )
    prepopulated_fields = {"slug":("title", )}


class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name", "post")

admin.site.register(Post, postAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(comment, CommentAdmin)
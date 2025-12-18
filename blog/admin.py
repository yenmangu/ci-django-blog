from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Customizes the admin interface for the Post model.
    It uses Summernote for the 'content' field and provides
    list display, search, filtering, and slug prepopulation.
    """

    list_display = ("title", "slug", "status", "created_on", "author")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


# Register your models here.
# admin.site.register(Post)
admin.site.register(Comment)

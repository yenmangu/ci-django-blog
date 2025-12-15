from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    # The path for editing a comment should capture the post's slug and the comment's ID.
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        view=views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        view=views.delete_comment,
        name="comment_delete",
    ),
]

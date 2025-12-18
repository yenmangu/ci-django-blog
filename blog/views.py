from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpRequest
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of `paginate_by` posts.

    **Context**
    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page

    **Template**
    :template:`blog/index.html`


    Returns:
        an invocation of the `django.shortcuts` `render()`
        function, called to render the template,
        and pass in  the context.
    """

    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context.get("page_obj")
        print("DEBUG page_obj: ", page_obj)

        return context


def post_detail(request: HttpRequest, slug):
    """Display an individual :model:`blog.Post`

    **Context**
        *All variables returned to the template*
    ``post``
        An instance of :model:`blog.Post`
    ``comments``
        All comments associated with the current :model:`blog.Post`
    ``comment_count``
        Number of comments
    ``comment_form``
        Form instance returned by :class:`CommentForm`, for leaving comments.
    **Template**
    :template:`blog/post_detail.html`.

    Args:
        request (HttpRequest): The incoming HttpRequest object
        slug (str): The slug to use to for the post get_object_or_404 method
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("receiving post request")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Content submitted and awaiting approval"
            )

    comment_form = CommentForm()
    print("About to render form")
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "coder": "RobShelford",
        },
    )


def comment_edit(request: HttpRequest, slug: str, comment_id: int):
    """View to edit comments

    Args:
        request (HttpRequest): The request object
        slug (str): The unique slug
        comment_id (int): Unique comment id integer
    """

    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def delete_comment(request: HttpRequest, slug: str, comment_id: int):
    """view to delete a comment

    Args:
        request (HttpRequest): Request object
        slug (str): Slug of the comment
        comment_id (int): ID of the comment
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))

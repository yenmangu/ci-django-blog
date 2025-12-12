from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
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

    ``post``
        An instance of :model:`blog.Post`

    **Template**

    :template:`blog/post_detail.html`.

    Args:
        request (HttpRequest): The incoming HttpRequest object
        slug (str): The slug to use to for the post get_object_or_404 method
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request, "blog/post_detail.html", {"post": post, "coder": "RobShelford"}
    )

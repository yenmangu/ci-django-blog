# Standard lib imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib import messages

# 3rd party imports
# Local imports
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about(request: HttpRequest):
    """
    Renders the most recent information on the website author and allows user collaboration requests.
    Displays an individual instance of "model:`about.Author`

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``Collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`

    :param request: Description
    :type request: HttpRequest
    """
    about_detail = About.objects.all().order_by("-updated_on").first()

    if request.method == "POST":
        collab_form = CollaborateForm(data=request.POST)

        if collab_form.is_valid():
            collab = collab_form.save()
            collab.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )

    collab_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about_detail, "collaborate_form": collab_form},
    )

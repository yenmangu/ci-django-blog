from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about(request: HttpRequest):
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
        {"about_detail": about_detail, "collaborate_form": collab_form},
    )

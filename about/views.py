from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import About

# Create your views here.


def about(request: HttpRequest):
    about_detail = About.objects.all().order_by("-updated_on").first()
    return render(request, "about/about.html", {"about_detail": about_detail})

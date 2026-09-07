from django.shortcuts import render, redirect
from .models import ContactMessage, Project
from django.contrib import messages


def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(
            request,
            "Thank you! Your message has been sent successfully."
        )

        return redirect("home")

    projects = Project.objects.all()

    return render(
        request,
        "portfolio/home.html",
        {
            "projects": projects
        }
    )
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import *

from main.models import *


def show_main(request):
    context = {
        "full_name": "Elvis Sestomi",
        "name": "Elvis",
        "npm": "2506544990",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia, Expected to graduate in 2029. Interested in Cyber Security and Web Development."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Elvis",
        "experience_list": Experience.objects.all()[::-1],
    }
    return render(request, "experience.html", context)

def show_certification(request):
    context = {
        "name": "Elvis",
        "certification_list": Certification.objects.all()[::-1],
    }
    return render(request, "certification.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Elvis",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")
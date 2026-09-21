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


# EXPERIENCE ACTION
def show_experience(request):
    context = {
        "name": "Elvis",
        "experience_list": Experience.objects.all()[::-1],
    }
    return render(request, "experience.html", context)


# CERTIFICATION ACTION
def show_certification(request):
    json_response = get_cert_json(request)
    
    cert = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    cert = [certif.object for certif in cert]
    context = {
        "name": "Elvis",
        "certification_list": cert,
    }
    return render(request, "certification.html", context)

def get_cert_json(request):
    title_query = request.GET.get("title", "").strip()
    cert = Certification.objects.all()

    if title_query:
        cert = cert.filter(title__icontains=title_query)

    certs_json = serializers.serialize("json", cert)
    return HttpResponse(certs_json, content_type="application/json")

def create_certification(request):
    form = CertificationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if request.POST.get("password") == "test":
            form.save()
            messages.success(request, "Sertifikasi baru berhasil ditambahkan!")
            return redirect("main:show_certification")
    context = {
        "name": "Elvis",
        "form": form,
    }
    return render(request, "cert_form.html", context)

def delete_cert(request, id):
    cert = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        if request.POST.get("password") == "test":
            cert.delete()
            messages.success(request, "Sertifikasi berhasil dihapus!")
            return redirect("main:show_certification")
        
    return redirect("main:show_certification")

def edit_cert(request, id):
    cert = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        form = CertificationForm(request.POST, instance=cert)

        if form.is_valid() and request.POST.get("password") == "test":
            form.save()
            return redirect("main:show_certification")

    else:
        form = CertificationForm(instance=cert)

    context = {
        "name": "Elvis",
        "form": form,
        "cert": cert,
    }

    return render(request, "cert_form_edit.html", context)

# PROJECT ACTION
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if request.POST.get("password") == "test":
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")
    context = {
        "name": "Elvis",
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
        if request.POST.get("password") == "test":
            project.delete()
            messages.success(request, "Project berhasil dihapus!")
            return redirect("main:show_projects")

    return redirect("main:show_projects")
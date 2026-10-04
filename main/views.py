from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from main.forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini
import datetime

from main.models import *

def is_editor(user):
    return user.groups.filter(name='Editor').exists()

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Elvis",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        next_url = request.POST.get("next")
        
        if not(next_url) or url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
            next_url="/"

        response = redirect(next_url)
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Elvis",
        "form": form,
        "next": request.GET.get("next", ""),
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "full_name": "Elvis Sestomi",
        "name": "Elvis",
        "npm": "2506544990",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia, Expected to graduate in 2029. Interested in Cyber Security and Web Development."
        ),
        "last_login": last_login,
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
    title_query = request.GET.get("course_name", "").strip()
    cert = Certification.objects.all()

    if title_query:
        cert = cert.filter(course_name__icontains=title_query)

    certs_json = serializers.serialize(
        "json", cert, use_natural_foreign_keys=True # Tambahkan argumen ini
    )
    return HttpResponse(certs_json, content_type="application/json")

@login_required(login_url="/login/")  # Tambahkan baris ini
def create_certification(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = CertificationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Sertifikasi baru berhasil ditambahkan!")
        return redirect("main:show_certification")
    context = {
        "name": "Elvis",
        "form": form,
    }
    return render(request, "cert_form.html", context)

@login_required(login_url="/login/")  # Tambahkan baris ini
def delete_cert(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    cert = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        cert.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
        return redirect("main:show_certification")
        
    return redirect("main:show_certification")

@login_required(login_url="/login/")  # Tambahkan baris ini
def edit_cert(request, id):
    if not(is_editor(request.user) or request.user.is_superuser):
        raise PermissionDenied

    cert = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        form = CertificationForm(request.POST, instance=cert)

        if form.is_valid():
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

@login_required(login_url="/login/")
def toggle_star_cert(request, cert_id):
    cert = get_object_or_404(Certification, pk=cert_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in cert.starred_by.all():
            cert.starred_by.remove(request.user)
        else:
            cert.starred_by.add(request.user)

    return redirect("main:show_certification")



# PROJECT ACTION
@login_required(login_url="/login/")  # Tambahkan baris ini
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
    context = {
        "name": "Elvis",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Elvis",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")  # Tambahkan baris ini
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
        

    return redirect("main:show_projects")

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
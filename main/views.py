from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Elvis",
        "npm": "2506544990",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia, Expected to graduate in 2029. Interested in Cyber Security and Web Development"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Burhan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
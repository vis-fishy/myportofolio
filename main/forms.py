from django.forms import *

from main.models import Project, Certification



class ProjectForm(ModelForm):
    password = CharField(
        label="Password",
        widget=PasswordInput,
    )

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }


class CertificationForm(ModelForm):
    password = CharField(
            label="Password",
            widget=PasswordInput,
        )
    class Meta:
        model = Certification
        fields = [
            "thumbnail",
            "publisher",
            "course_name",
            "year_display",
            "verification_url",
        ]

        labels = {
            "thumbnail": "Icon Penerbit",
            "publisher": "Nama Penerbit",
            "course_name": "Nama Prestasi/Course",
            "year_display": "Tahun Terbit",
            "verification_url": "Link Verifikasi",
        }

        widgets = {
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "publisher": TextInput(
                attrs={
                    "placeholder": "Coursera",
                }
            ),
            "course_name": TextInput(
                attrs={
                    "placeholder": "Basic of Prompt Engineering",
                }
            ),
            "year_display": TextInput(
                attrs={
                    "placeholder": "YYYY",
                }
            ),
            "verification_url": URLInput(
                attrs={
                    "placeholder": "Your verification link",
                }
            ),
        }
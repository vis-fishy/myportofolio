from django.forms import *

from main.models import Project, Certification
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


class ProjectForm(ModelForm):
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class CertificationForm(ModelForm):
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

    def clean_year_display(self):
        year_input = strip_tags(self.cleaned_data["year_input"]).strip()
        if not year_input:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return year_input
    
    def clean_publisher(self):
        publisher = strip_tags(self.cleaned_data["publisher"]).strip()
        if not publisher:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return publisher

    def clean_course_name(self):
        course_name = strip_tags(self.cleaned_data["course_name"]).strip()
        if not course_name:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return course_name
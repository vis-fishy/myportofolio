import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.CharField(max_length=255, default='NOT ADDED YET')
    title = models.CharField(max_length=255)
    description = models.JSONField(default=list)
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    time_range_display = models.CharField(max_length=255, default='Mmm yyyy - Mmm yyyy')
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
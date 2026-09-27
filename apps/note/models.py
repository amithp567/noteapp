from django.db import models
import uuid

class Note(models.Model):
    class Priority(models.TextChoices):
        HIGH = "HIGH", "High"
        MEDIUM = "MEDIUM", "Medium"
        LOW = "LOW", "Low"

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True
    )
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    priority = models.CharField(
        max_length=30,
        choices=Priority.choices,
        default=Priority.LOW
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.title}"

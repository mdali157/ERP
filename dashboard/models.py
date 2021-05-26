from django.db import models


# Create your model here.
from testing.models import Bugs


class Requirement(models.Model):
    status_choices = (
        ("IN PROGRESS", "IN PROGRESS"),
        ("COMPLETED", "COMPLETED"),
        ("VERIFIED", "VERIFIED")

    )
    status = models.CharField(max_length=100, choices=status_choices)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title


class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    projectDescription = models.TextField(max_length=5000)
    requirement = models.ManyToManyField(Requirement, default=None)
    status=models.TextField(max_length=50, null=True)
    date= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    bugs = models.ManyToManyField(Bugs, default=None)

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import ProjectModel,Requirement

# Register your model here.

admin.site.register(ProjectModel)
admin.site.register(Requirement)
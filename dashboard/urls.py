from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls import url
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('projects', views.project_view, name='project_view'),
    path('addproject', views.addProject, name='addproject'),
    path('addrequirement/<id>/', views.add_requrement, name='addrequirement'),
    path('deleterequirments/<id>/', views.delete_requirment, name='deleterequirment'),
    path('projects/<id>/', views.delete_project, name='deleteproject'),
    path('updateProject/<id>/', views.update_project, name='updateproject'),
    path('projectdetails/<id>', views.project_detail, name='projectdetail'),
    path('updateRequirement/<id>/', views.update_requirements, name='updaterequirement'),

]
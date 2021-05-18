from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'attendance'

urlpatterns = [

    path('attendanceview', views.attendanceview, name='attendanceview'),

]

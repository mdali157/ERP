from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'testing'

urlpatterns = [

    path('testingview/', views.testingview, name='testingview'),
    path('addBug/', views.addBug, name='addBug'),
    path('deletebug/<id>/', views.deletebug, name='deletebug'),
    path('updatebug/<id>', views.updatebug, name='updatebug'),
    # url(r'^(?P<id>[\w-]+)/$', views.employee_detail, name='employeedetail'),
    path('bug_detail/<id>', views.bug_detail, name='bug_detail'),
]

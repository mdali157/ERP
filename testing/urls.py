from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'testing'

urlpatterns = [

    path('testingview/', views.testingview, name='testingview'),
    path('addBug/', views.addBug, name='addBug'),
    path('deletebug/<id>/', views.deletebug, name='deletebug'),
    path('updatebug/<id>', views.updatebug, name='updatebug'),
    path('bug_detail/<id>', views.bug_detail, name='bug_detail'),
    path('bug_form', views.form_2, name='form2')
]

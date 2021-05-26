from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'testing'

urlpatterns = [

    path('Test-Projects/', views.Testprojects, name='Testprojects'),
    # path('addBug/', views.addBug, name='addBug'),
    # path('deletebug/<id>/', views.deletebug, name='deletebug'),
    path('updatebug/<id>', views.update_bugs, name='updatebug'),
    path('Projects_bugs/<id>', views.Projects_bugs, name='Projects_bugs'),
    path('addbug/<id>/', views.addbug, name='addbug'),
    path('delete_bug/<id>', views.delete_bug, name='delete_bug')

]

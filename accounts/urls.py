from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('logout', views.logout_views, name='logout'),
    path('login', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

]

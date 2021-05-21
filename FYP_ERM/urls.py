
from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard', include('dashboard.urls')),
    path('employee/', include('employee.urls')),
    path('attendance/', include('attendance.urls')),
    path('testing/', include('testing.urls')),
    path('', dashview.dashboard_view),
    path('client/',views.client,name='client')
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
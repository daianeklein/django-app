from django.contrib import admin
from django.urls import path
from file_example import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('upload/', views.upload, name = 'upload'),
    path('file_successfully_uploaded/', views.uploaded_file, name = 'file_successfully_uploaded')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT,
        )

from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from clip.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name="index"),
    path('', youtube, name="index"),
        path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

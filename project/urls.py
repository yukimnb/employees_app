from django.contrib import admin
from django.urls import path, include
from . import settings_common, settings_dev
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("employees.urls")),
] + static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)

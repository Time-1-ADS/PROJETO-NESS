from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('player.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# settings.py (update for media files)
MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
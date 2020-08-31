from django.contrib import admin
from django.urls import path, include
from services import views
import services
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', services.views.home, name='navhome'),
                  path('accounts/', include('accounts.urls')),
                  path('services/', include('services.urls')),
                  path('aboutus/', include('aboutus.urls')),
                  path('equipment/', include('equipment.urls')),
                  path('projects/', include('projects.urls')),
                  path('filer2/', include('filer.urls')),
                  path('filer/', include('filer.server.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

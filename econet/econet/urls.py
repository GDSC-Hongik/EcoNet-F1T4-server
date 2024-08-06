from django.contrib import admin
from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('users/', include('users.urls')),
    path('boards/', include('boards.urls')),
    path('todays/', include('todays.urls')),
    path('maps/', include('maps.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
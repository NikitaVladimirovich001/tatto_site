from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('sitetatto/', include('sitetatto.urls')),
    path('record/', include('record.urls')),
    path('mastera/', include('mastera.urls')),
   # path('comment/', include('comment.urls')),
    path('comment/', include(('comment.urls', 'comments'), namespace='comment')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Auth
    path('api-auth/', include('rest_framework.urls')),

    #API
    path('api/', include('api.urls')),

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
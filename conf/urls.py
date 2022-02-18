from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import *
from shops.rest.restinterface import OrganizationsAsJSON, ShopsAsJSON
from filebrowser.sites import site


router = routers.DefaultRouter()
router.register(r'api/organizations', OrganizationsAsJSON)
router.register(r'api/shops', ShopsAsJSON)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

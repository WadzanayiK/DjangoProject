from django.contrib import admin
from django.urls import path, include
from musicapp import urls as musicapp_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include ('musicapp.urls'))
]

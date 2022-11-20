
from django.contrib import admin
from django.urls import path, include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Services.urls')),
    re_path(r'^chaining/', include('smart_selects.urls')),
]

from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='appointment'), name='home'),
    path('service/', include('Services.urls')),
    re_path(r'^chaining/', include('smart_selects.urls')),
]

from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', RedirectView.as_view(pattern_name='appointment'), name='home'),
    path('', include('Services.urls')),
    re_path(r'^chaining/', include('smart_selects.urls')),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


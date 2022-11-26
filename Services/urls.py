from django.urls import path
from django.views.generic import RedirectView
from .import views

urlpatterns = [
    path('index', views.Index, name='index'),
    #path('', views.AppointmentListView.as_view(), name='appointment'),
    path('', views.AppointmentCreateView.as_view(), name='appointment'),
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-extra-info/', views.load_extra_info, name='ajax_load_extra_info'),
    path('ajax/load-pricing/', views.load_pricing, name='ajax_load_pricing'),
    path('ajax/load-image/', views.load_category_image, name='ajax_load_category_image'),
    
   #path('ajax/load-pricing/', views.load_name, name='ajax_load_name'),
    path('ajax/load-consultants/', views.load_consultants, name='ajax_load_consultants'),
]

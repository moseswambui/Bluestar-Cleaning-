from django.urls import path
from django.views.generic import RedirectView
from .import views

urlpatterns = [
    #path('', views.get_data, name='index'),
    #path('', views.AppointmentListView.as_view(), name='appointment'),
    path('', views.AppointmentCreateView.as_view(), name='appointment'),
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-consultants/', views.load_consultants, name='ajax_load_consultants'),
]

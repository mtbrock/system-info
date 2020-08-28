from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('system-info/', views.system_info, name='system-info'),
]

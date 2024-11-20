from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('group/', views.group, name='group_page'),
    path('download_group', views.download_group, name='download_group'),
    path('download_member', views.download_member, name='download_member'),
]

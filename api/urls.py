from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='api-overview'),
    # groups
    path('group-list/', views.GroupList, name='group-lists'),
    path('group-create/', views.createGroup, name='group-create'),
    path('group-update/<str:pk>/', views.updateGroup, name='group-update'),
    path('group-detail/<str:pk>/', views.detailGroup, name='group-detail'),
    path('group-delete/<str:pk>/', views.deleteGroup, name='group-delete'),
    
    # members
    path('member-list/', views.memberList, name='member-lists'),
    path('member-create/', views.memberCreate, name='member-create'),
    
    
    # path('member-list', views.MemberList, name='member-lists'),
    
    
    
]

from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),  #projects/<pk>
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),  #pledges/<pk>
    path('beefriends/', views.BeefriendList.as_view()),
    path('beefriends/<int:pk>/', views.BeefriendDetail.as_view()),
    path('get-suburbs/', views.get_all_suburbs),
]

urlpatterns = format_suffix_patterns(urlpatterns)
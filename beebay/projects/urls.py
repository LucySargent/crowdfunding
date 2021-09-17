from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),  #projects/<pk>
    path('pledges/', views.PledgeList.as_view()),
    path('beefriends/', views.BeefriendList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
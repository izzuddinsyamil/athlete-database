from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

app_name = 'api'
urlpatterns = [
    path('', views.SexList.as_view()),
    path('sex/', views.SexList.as_view()),

    # athlete
    path('athlete/', views.AthleteList.as_view()),
    path('athlete/<int:pk>/', views.AthleteDetail.as_view()),
    path('athlete/sort/<str:sortby>/', views.AthleteSorted.as_view()),

    # achievements
    path('achievement/', views.AchievementList.as_view()),
    path('achievement/<int:pk>', views.AchievementDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

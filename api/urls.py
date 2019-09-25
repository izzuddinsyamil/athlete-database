from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

app_name = 'api'
urlpatterns = [
    # athlete
    path('athlete/', views.AthleteList.as_view()),
    path('athlete/<int:pk>/', views.AthleteDetail.as_view()),
    path('athlete/sort/<str:sortby>/', views.AthleteSorted.as_view()),

    # achievements
    path('achievement/', views.AchievementList.as_view()),
    path('achievement/<int:pk>', views.AchievementDetail.as_view()),

    # event
    path('event/', views.EventList.as_view()),
    path('event/<int:pk>', views.EventDetail.as_view()),

    # achievement mapping
    path('achievement-mapping/', views.AchievementMappingList.as_view()),
    path('achievement-mapping/<int:pk>',
         views.AchievementMappingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

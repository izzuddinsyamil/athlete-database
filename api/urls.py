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
    path('achievement/', views.CollectionList.as_view()),
    path('achievement/<int:pk>', views.CollectionDetail.as_view()),

    # event
    path('event/', views.EventList.as_view()),
    path('event/<int:pk>', views.EventDetail.as_view()),

    # achievement mapping
    path('achievement-mapping/', views.AchievementMappingList.as_view()),
    path('achievement-mapping/<int:pk>',
         views.AchievementMappingDetail.as_view()),

    # achievement list
    path('achievement-list/', views.AchievementCollectionList.as_view()),
    path('achievement-list/<int:pk>',
         views.AchievementCollectionDetail.as_view()),

     # sport
    path('sport/', views.SportList.as_view()),
    path('sport/<int:pk>',
         views.SportDetail.as_view()),

     # athlete sports
    path('athlete-sports/', views.AthleteSportsList.as_view()),
    path('athlete-sports/<int:pk>',
         views.AthleteSportsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

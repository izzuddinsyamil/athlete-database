from django.urls import path

from . import views

app_name = 'athletedb'
urlpatterns = [
    # frontend
    path('', views.index, name='index'),
    path('atlet/<int:athlete_id>/', views.athlete_detail, name='athlete-detail'),
    path('prestasi/<int:achievement_id>/',
         views.achievement_detail, name='achievement-detail'),

]

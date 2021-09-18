from django.shortcuts import render
from athletedb.models import (
    Athlete, Achievement, Event,
    AchievementList, AchievementMapping, Sport, AthleteSports)
from rest_framework import viewsets, generics
from api.serializers import (
    AthleteSerializer,
    AchievementSerializer, EventSerializer,
    AchievementListSerializer,
    AchievementMappingSerializer,
    SportSerializer,
    AthleteSportsSerializer)

# Create your views here.

from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# paginator = PageNumberPagination()

class AthleteList(generics.ListCreateAPIView):
    serializer_class = AthleteSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        athlete_list = Athlete.objects.all()
        if 'athlete' in self.request.query_params:
            athlete_name = self.request.query_params['athlete']
            athlete_list = athlete_list.filter(
                name__icontains=athlete_name)

        if 'sports' in self.request.query_params:
            sport_name = self.request.query_params['sports']
            athlete_list = athlete_list.filter(
                sports__name__icontains=sport_name
            )

        return athlete_list


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    pagination_class = MyPagination


class AthleteSorted(generics.ListAPIView):
    serializer_class = AthleteSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        sortby = self.kwargs['sortby']
        return Athlete.objects.order_by(sortby)


class CollectionList(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = MyPagination


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = MyPagination


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = MyPagination


class AchievementCollectionList(generics.ListCreateAPIView):
    queryset = AchievementList.objects.all()
    serializer_class = AchievementListSerializer
    pagination_class = MyPagination


class AchievementCollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AchievementList.objects.all()
    serializer_class = AchievementListSerializer
    pagination_class = MyPagination


class SportList(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    pagination_class = MyPagination


class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    pagination_class = MyPagination


class AthleteSportsList(generics.ListCreateAPIView):
    queryset = AthleteSports.objects.all()
    serializer_class = AthleteSportsSerializer
    pagination_class = MyPagination


class AthleteSportsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AthleteSports.objects.all()
    serializer_class = AthleteSportsSerializer
    pagination_class = MyPagination


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = MyPagination


class AchievementMappingList(generics.ListCreateAPIView):
    serializer_class = AchievementMappingSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        try:
            id = self.request.query_params['id']
            return AchievementMapping.objects.filter(athlete__id=id)
        except:
            return AchievementMapping.objects.all()


class AchievementMappingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AchievementMapping.objects.all()
    serializer_class = AchievementMappingSerializer
    pagination_class = MyPagination

from django.shortcuts import render
from athletedb.models import (
    Sex, Athlete, Achievement, Event,
    AchievementList, AchievementMapping)
from rest_framework import viewsets, generics
from api.serializers import (
    SexSerializer, AthleteSerializer,
    AchievementSerializer, EventSerializer,
    AchievementListSerializer,
    AchievementMappingSerializer)

# Create your views here.


class SexList(generics.ListCreateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer


class AthleteList(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class AthleteSorted(generics.ListAPIView):
    serializer_class = AthleteSerializer

    def get_queryset(self):
        sortby = self.kwargs['sortby']
        return Athlete.objects.order_by(sortby)


class AchievementList(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class AchievementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AchievementMappingList(generics.ListCreateAPIView):
    serializer_class = AchievementMappingSerializer

    def get_queryset(self):
        try:
            id = self.request.query_params['id']
            return AchievementMapping.objects.filter(athlete__id=id)
        except:
            return AchievementMapping.objects.all()


class AchievementMappingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AchievementMapping.objects.all()
    serializer_class = AchievementMappingSerializer

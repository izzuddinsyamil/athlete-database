from athletedb.models import (
    Athlete, Sex, Sport, Achievement,
    AchievementMapping, Event,
    AchievementList)
from rest_framework import serializers


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ('name',)


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('name',)


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id',
            'title',
            'description',
            'position',
            'organizer',
            'location',
            'date',)


class AthleteSerializer(serializers.ModelSerializer):
    sports = SportSerializer(many=True, read_only=True)

    class Meta:
        model = Athlete
        fields = (
            'id',
            'name',
            'nik',
            'email',
            'birth_date',
            'birth_place',
            'age',
            'phone_number',
            'address',
            'school',
            'sex',
            'sports',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AchievementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementList
        fields = '__all__'


class AchievementMappingSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer()
    event = EventSerializer()
    achievement = AchievementListSerializer()

    class Meta:
        model = AchievementMapping
        fields = (
            'id', 'athlete',
            'event', 'achievement')

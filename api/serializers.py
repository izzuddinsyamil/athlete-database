from athletedb.models import (
    Athlete, Sport, Achievement,
    AchievementMapping, Event,
    AchievementList)
from rest_framework import serializers


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('name',)


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id', 'description',
            'result', 'level',
            'certificate_file',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AchievementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementList
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    sports = SportSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Athlete
        fields = (
            'id',
            'name',
            'nik',
            'photo',
            'email',
            'birth_date',
            'birth_place',
            'age',
            'blood_type',
            'phone_number',
            'address',
            'school',
            'sex',
            'sports',
            'achievements'
        )


class AchievementMappingSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer()
    event = EventSerializer()
    achievement = AchievementListSerializer()

    class Meta:
        model = AchievementMapping
        fields = (
            'id', 'athlete',
            'event', 'achievement')

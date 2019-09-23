from athletedb.models import Athlete, Sex, Sport, Achievement
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
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Athlete
        fields = (
            'id',
            'name',
            'birth_date',
            'age',
            'phone_number',
            'address',
            'school',
            'sex',
            'sports',
            'achievements',
        )

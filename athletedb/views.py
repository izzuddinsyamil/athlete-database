from django.shortcuts import (
    render, get_object_or_404)
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Athlete, Achievement
from django.http import JsonResponse


# Create your views here.


def index(request):
    athlete_list = Athlete.objects.all()

    context = {
        'athlete_list': athlete_list,
    }
    return render(request, 'athletedb/index.html', context)


def athlete_detail(request, athlete_id):
    athlete_detail = get_object_or_404(Athlete, pk=athlete_id)
    return render(
        request,
        'athletedb/athlete_detail.html',
        {'athlete_detail': athlete_detail, }
    )


def achievement_detail(request, achievement_id):
    achievement_detail = get_object_or_404(Achievement, pk=achievement_id)
    return render(
        request,
        'athletedb/achievement_detail.html',
        {'achievement_detail': achievement_detail, }
    )

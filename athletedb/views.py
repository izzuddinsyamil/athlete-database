from django.shortcuts import (
    render, get_object_or_404)
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Athlete, Achievement
from django.http import JsonResponse
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger)

# pylint: disable=no-member


def index(request):
    athlete_list = Athlete.objects.all()

    athlete_name = request.GET.get('athlete')
    if athlete_name:
        athlete_list = athlete_list.filter(
            name__icontains=athlete_name)

    sport_name = request.GET.get('sports')
    if sport_name:
        athlete_list = athlete_list.filter(
            sports__name__icontains=sport_name
        )

    page = request.GET.get('page', 1)

    paginator = Paginator(athlete_list, 20)

    try:
        athletes = paginator.page(page)
    except PageNotAnInteger:
        athletes = paginator.page(1)
    except EmptyPage:
        athletes = paginator.page(paginator.num_pages)

    context = {
        'athlete_list': athletes,
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

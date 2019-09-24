from django.shortcuts import (
    render, get_object_or_404)
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Athlete, Achievement
from django.http import JsonResponse
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger)

# pylint: disable=no-member
# Create your views here.


def index(request):
    athlete_list = Athlete.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(athlete_list, 10)

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

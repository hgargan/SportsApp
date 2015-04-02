from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from roster.models import Athlete, Event, Team

def home(request):
    context = {
        'athlete_count': Athlete.objects.count(),
        'event_count': Event.objects.count(),
    }
    return render(request, 'roster/home.html', context)


    
def event(request, pk):
    event = get_object_or_404(Event, id=pk)
    event_athletes = event.athletes.all()
    return render(request, 'roster/event.html', {'event': event, 'event_athletes': event_athletes})

def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    return render(request, 'roster/team.html', {'team': team})

def team_athlete_list(request, team_pk):
    team = get_object_or_404(Team, id=team_pk)
    team_athletes = team.athletes.all()
    return render(request, 'roster/athlete_list.html', {'team_athletes': team_athletes})

def athlete(request, pk):
    athlete = get_object_or_404(Athlete, id=pk)
    return render(request, 'roster/athlete.html', {'athlete': athlete})

def eventList(request):
    event_list = Event.objects.all()
    return render(request, 'roster/event_list.html', {'events': event_list})


def teamList(request):
    team_list = Team.objects.all()
    return render(request, 'roster/team_list.html', {'teams': team_list})

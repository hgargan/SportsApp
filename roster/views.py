from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from roster.models import Athlete, Event, Team

def home(request):
    context = {
        'athlete_count': Athlete.objects.count(),
        'event_count': Event.objects.count(),
    }
    return render(request, 'roster/home.html', context)

def athlete(request, pk):
    athlete = get_object_or_404(Athlete, id=pk)
    return render(request, 'roster/athlete.html', {'athlete': athlete})
    
def event(request, pk):
    event = get_object_or_404(Event, id=pk)
    eventAthletes = get_object_or_404(Athlete.events,id=pk)
    return render(request, 'roster/event.html', {'event': event})

def athleteList(request):
    athlete_list = Athlete.objects.all()
    return render(request, 'roster/athlete_list.html', {'athletes': athlete_list})

def eventList(request):
    event_list = Event.objects.all()
    return render(request, 'roster/event_list.html', {'events': event_list})

def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    return render(request, 'roster/team.html', {'team': team})

def teamList(request):
    team_list = Team.objects.all()
    return render(request, 'roster/team_list.html', {'teams': team_list})
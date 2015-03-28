from django.contrib import admin
from roster.models import Athlete, Event, Team

class AthleteAdmin(admin.ModelAdmin):
    search_fields = ('lastname',)

admin.site.register(Athlete, AthleteAdmin)

class EventAdmin(admin.ModelAdmin):
    search_fields= ('name',)
    
admin.site.register(Event, EventAdmin)
admin.site.register(Team)
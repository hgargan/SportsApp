from django.db import models

class Team(models.Model):
    sport = models.CharField(unique=True, max_length=50)
    school = models.Charfield(unique=False, max_length=50)
    season = models.CharField(unique=True, max_length=50)
    coach = models.CharField(unique=True, max_length=50)
    athlete = models.OneToOneField('roster.Athlete')
    
    class Meta(object):
        verbose_name_plural = "Teams"
        ordering = ('school', 'sport', 'season')
        
    def __unicode__(self):
        return u'%s | %s'% (self.school, self.name)
    
        
class Event(models.Model):
    name = models.CharField(unique=True, max_length=50)
    players = models.ManyToManyField(Athlete)
    
    class Meta(object):
        verbose_name_plural = "Events"
        ordering = ('name')
        
    def __unicode__(self):
        return u'%s'% self.name
    

class Athlete(models.Model):
    name = models.CharField(unique=False, max_length=50)
    event = models.CharField(unique=False, max_length=50)
    year = models.CharField(unique=False, max_length=50)
    hometown = models.CharField(unique=False, max_length=50)
    highschool = models.CharField(unique=False, max_length=75)
    description = models.TextField(max_length=1000, default='')
    

    class Meta(object):
        verbose_name_plural = "Athletes"
        ordering = ('name', 'event', 'year', 'hometown', 'highschool')
        
    def __unicode__(self):
        return u'% %s' %(self.name, self.event)
    
    
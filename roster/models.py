from django.db import models

        
class Event(models.Model):
    name = models.CharField(unique=True, max_length=50)
    athletes = models.ManyToManyField('Athlete', related_name='events', null=True)
    
    class Meta(object):
        verbose_name_plural = "Events"
        ordering = ('name',)
        
    def __unicode__(self):
        return u'%s' % self.name
    

class Athlete(models.Model):
    lastname = models.CharField(unique=False, max_length=20, default='')
    firstname = models.CharField(unique=False, max_length=20, default='')
    #event = models.CharField(unique=False, max_length=50)
    year = models.CharField(unique=False, max_length=50)
    hometown = models.CharField(unique=False, max_length=50)
    highschool = models.CharField(unique=False, max_length=75)
    description = models.TextField(default='')
    

    class Meta(object):
        verbose_name_plural = "Athletes"
        ordering = ('lastname', 'firstname', 'year', 'hometown', 'highschool')
        
    def __unicode__(self):
        return u'%s, %s' % (self.lastname, self.firstname)
    
class Team(models.Model):
    sport = models.CharField(unique=True, max_length=50)
    school = models.CharField(unique=False, max_length=50)
    season = models.CharField(unique=False, max_length=50, default='')
    coach = models.CharField(unique=True, max_length=50, default='')
    athletes = models.ManyToManyField('Athlete', related_name='teams', default='', null=True)
    
    class Meta(object):
        verbose_name_plural = "Teams"
        ordering = ('school', 'sport', 'season')
        
    def __unicode__(self):
        return u'%s | %s'% (self.school, self.sport)
    
    
from optparse import TitledHelpFormatter
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class Song(models.Model):  
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    release_date = models.DateField()
    likes = models.IntegerField()
    title =models.CharField(max_length =50)
        
class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)    
    content = models.CharField(max_length =50000)
    
                
    
        
        
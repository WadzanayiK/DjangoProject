from django.db import models
from django.utils import timezone

# Create your models here.

   
class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age=models.IntegerField(default='null')
	
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=400)
    date_released = models.DateField(null=True)
    likes = models.CharField(max_length=400)
    artiste_id = models.CharField(max_length=40,default='null')
    
    def __str__(self):
        return self.title
	
	

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)    
    content = models.CharField(max_length =50000)
	
def __str__(self):
		if len(self.content) > 100:
			return f'{self.content[0:100]}...'
		else:
			return f'{self.content}'
   

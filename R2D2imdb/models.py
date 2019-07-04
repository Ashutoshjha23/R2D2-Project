from django.db import models

# Create your models here.
class R2D2imdb(models.Model):
    id = models.IntegerField(primary_key=True)
    Name_of_movie = models.CharField(max_length=100,default=' ')
    Movie_Rating = models.CharField(max_length=10,default=' ')
    StarCast = models.CharField(max_length=300,default=' ')

    class Meta:
        db_table = 'R2D2imdb'

    def __str__(self):
        return self.Name_of_Movie

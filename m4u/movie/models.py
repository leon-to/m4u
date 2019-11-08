from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    release = models.DateField()
    description = models.CharField(max_length=500)
    poster = models.URLField(max_length=200)
    trailer = models.URLField(max_length=200)

    def __str__(self):
        return self.title + ' (' + self.release.__str__() + ')'

class Genre(models.Model):
    genre = models.CharField(max_length=30)

class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

from django.db import models

# Create your models here.
#Film model
class Film(models.Model):
    film_name = models.CharField(max_length=50)
    release_date = models.CharField(max_length =30, null=True)
    director_name = models.CharField(max_length=30, null=True)
    imdb_rating = models.FloatField(null=True)
    movie_runtime = models.IntegerField(null=True)
    movie_poster = models.CharField(max_length=256, null=True)
    poster = models.ImageField(upload_to= "media/posters/",
            null = True,
            blank = True,
            width_field=250,
            height_field=250
            )

    def __str__(self):
        return self.film_name
#Actor model
class Actor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor_name = models.CharField(max_length=30)

    def __str__(self):
        return self.actor_name
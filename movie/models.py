from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=150)
    decsription = models.TextField(max_length=500)
    duration = models.PositiveIntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=300)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



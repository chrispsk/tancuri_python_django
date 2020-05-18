from django.db import models

# Create your models here.
class Panzer(models.Model):
    tureta = models.IntegerField()
    engine = models.IntegerField()
    tracks = models.IntegerField()
    front = models.IntegerField()
    health = models.IntegerField()

    def __str__(self):
        return str(self.health)

class Abrams(models.Model):
    tureta = models.IntegerField()
    engine = models.IntegerField()
    tracks = models.IntegerField()
    front = models.IntegerField()
    health = models.IntegerField()

    def __str__(self):
        return str(self.health)


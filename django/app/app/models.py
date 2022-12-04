from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
#A room isnt always going to be a perfect square
#     _______________
#    /              /|
#   /              / |
#  /              /  |height
# /_____width____/   |
# /______________|   / 
# /______________|  /depth  
# /______________| /   
# /______________|/ 
#For use with flask in a dockerfile
from django.db import models
from django.utils.text import slugify

class Room(models.Model):
    name = models.CharField(max_length=12)
    slug = models.SlugField(max_length = 12, unique=True, null = True)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)
    def calculatePaintWalls(self):
        # One roof with four sides of two possible different lengths, exclude painting the floor.
        area = self.width*self.depth + 2 * self.height*self.depth + 2 * self.height*self.width
        return area
    def calculateFloorArea(self):
        return self.width*self.depth
    def calculateRoomVolume(self):
        return self.width*self.depth*self.height
    def __str__(self):
        return self.name


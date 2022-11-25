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
import unittest

class Room:
    def __init__(self, w, d, h): 
        self.depth = w
        self.height = d
        self.width = h
        
    def calculateArea(self):
        # One roof with four sides of two possible different lengths, exclude painting the floor.
        return self.width*self.depth + 2 * self.height*self.depth + 2 * self.height*self.width

def mainfun():
    paint = Room(2,3,4)
    area = paint.calculateArea()
    print('The area is::: ', str(area))

if __name__ == "__main__":
    mainfun()

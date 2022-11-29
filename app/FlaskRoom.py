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
class FlaskRooms:
    def __init__(self, w=0, d=0, h=0):
        self.width = float(w)
        self.depth = float(d)
        self.height = float(h)
    def calculatePaintWalls(self):
        # One roof with four sides of two possible different lengths, exclude painting the floor.
        area = self.width*self.depth + 2 * self.height*self.depth + 2 * self.height*self.width
        return area
    def calculateFloorArea(self):
        return self.width*self.depth
    def calculateRoomVolume(self):
        return self.width*self.depth*self.height

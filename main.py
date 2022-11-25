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

class Rooms:
    def __init__(self, w=0, d=0, h=0):
        self.rooms=[]
        self.depth = w
        self.height = d
        self.width = h   
    def calculatePaintWalls(self):
        # One roof with four sides of two possible different lengths, exclude painting the floor.
        area = self.width*self.depth + 2 * self.height*self.depth + 2 * self.height*self.width
        return area
    def calculateFloorArea(self):
        return self.width*self.depth
    def calculateRoomVolume(self):
        return self.width*self.depth*self.width*self.height
def roominateFun(*args):
    print(args[0][0],args[0][0],args[0][0])
    task = Rooms(float(args[0][0]),float(args[0][0]),float(args[0][0]))
    task.rooms.append(task)
    for j in task.rooms:
        how_much_paint = j.calculatePaintWalls()
        floor_area = j.calculateFloorArea()
        room_volume = j.calculateRoomVolume()
        print('The floor area is::: {} The room volume is::: {} How much paint::: {}'
              .format(floor_area,room_volume,how_much_paint))
    return roominateFun(input("Enter another room of any width, height, depth: "))

if __name__ == "__main__":
    roominateFun(input("Enter another room of any width, height, depth: "))

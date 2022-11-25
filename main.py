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
#Currently runs in single characters only with no spaces on the command line
#for example, 123, is equivalent to width height and depth 1 2 3.
class Room:
    def __init__(self, args):
        self.depth = int(args[0][0])
        self.height = int(args[0][1])
        self.width = int(args[0][2])
        print(self.depth,self.height,self.width)
    def calculatePaintWalls(self):
        # One roof with four sides of two possible different lengths, exclude painting the floor.
        area = self.width*self.depth + 2 * self.height*self.depth + 2 * self.height*self.width
        return area
    def calculateFloorArea(self):
        return self.width*self.depth
    def calculateRoomVolume(self):
        return self.width*self.depth*self.width*self.height
def roominateFun(*args):
    room = Room(args)
    rooms.append(room)
    for j in rooms:
        ###calculates everytime the room is added so might need to tweak at large scales of room numbers
        how_much_paint = j.calculatePaintWalls() 
        floor_area = j.calculateFloorArea()
        room_volume = j.calculateRoomVolume()
        print(rooms.index(j),')The floor area is::: {} The room volume is::: {} How much paint::: {}'
              .format(floor_area,room_volume,how_much_paint))
    return roominateFun(input("Enter another room of any width, height, depth: "))
if __name__ == "__main__":
    rooms=[]
    roominateFun(input("Enter another room of any width, height, depth: "))

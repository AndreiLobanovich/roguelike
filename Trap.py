from Tile import Tile
from random import randint


class Trap(Tile):
    def __init__(self, imgs, tileType):
        super().__init__(imgs, tileType)
        self.calldown = randint(500, 1000)
        self.current_time = randint(0, self.calldown)
        self.hitCalldown = 0
        self.active = True

    def process(self):
        self.imgNumber = int(self.active)
        if self.hitCalldown:
            self.hitCalldown -= 1
        if self.current_time:
            self.current_time -= 1
        else:
            self.current_time = self.calldown
            self.active = not self.active

    def hit(self):
        if self.active:
            if not self.hitCalldown:
                self.hitCalldown = 300
                return True
        return False



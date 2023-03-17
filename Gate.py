from Tile import Tile


class Gate(Tile):
    def __init__(self, imgs, speciality):
        tileType = "door"
        super().__init__(imgs, tileType, speciality)

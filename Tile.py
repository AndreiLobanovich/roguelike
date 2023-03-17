from constants import TILE_SIZE, SCALE_FACTOR


class Tile:
    def __init__(self, imgs, tileType, speciality=None):
        self.tileType = tileType
        self.imgs = imgs
        self.speciality = speciality
        self.imgNumber = 0

    def display(self, screen, x, y):
        width = SCALE_FACTOR * TILE_SIZE
        rect = self.imgs[0].get_rect(topleft=(x * width, y * width))
        screen.blit(self.imgs[self.imgNumber], rect)

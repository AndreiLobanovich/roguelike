from constants import TILE_SIZE, SCALE_FACTOR, playerTile, directions
from utils import getTiles


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lastDirection = "none"
        self.shift = [x - 2, y - 2]
        i, j = playerTile["pos"]
        self.animation = 100
        self.imgs = getTiles(playerTile["path"], i, j)
        self.rect = self.imgs[0].get_rect(
            topleft=(self.x * TILE_SIZE * SCALE_FACTOR, self.y * TILE_SIZE * SCALE_FACTOR)
        )

    def display(self, screen, chunkCords):
        self.animation -= 1
        self.animation = 100 if self.animation == 0 else self.animation
        x1, y1 = chunkCords[0] + directions[self.lastDirection][0], chunkCords[2] + directions[self.lastDirection][1]
        self.rect = self.imgs[0].get_rect(
            topleft=(
                (2 - (x1 - self.x + 2) + directions[self.lastDirection][0]) * TILE_SIZE * SCALE_FACTOR,
                (2 - (y1 + 2 - self.y) + directions[self.lastDirection][1]) * TILE_SIZE * SCALE_FACTOR
            )

        )
        screen.blit(self.imgs[self.animation > 50], self.rect)

    def move(self, direction):
        self.x, self.y = self.x + directions[direction][0], self.y + directions[direction][1]
        self.lastDirection = direction
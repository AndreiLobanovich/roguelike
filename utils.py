import pygame
from constants import TILE_SIZE, SCALE_FACTOR


def getTiles(paths, x, y):
    tiles = []
    for path in paths:
            image = pygame.image.load(path).convert().subsurface([
                    TILE_SIZE * (x - 1),
                    TILE_SIZE * (y - 1),
                    TILE_SIZE * x,
                    TILE_SIZE * y,
                ])
            image = pygame.transform.scale(image, (TILE_SIZE * SCALE_FACTOR, TILE_SIZE * SCALE_FACTOR))
            tiles.append(image)
    return tiles

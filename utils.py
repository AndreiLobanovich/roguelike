import pygame
from constants import TILE_SIZE, SCALE_FACTOR


def getTiles(paths, x, y):
    tiles = []
    for path in paths:
        image = pygame.image.load(path).convert().subsurface([
                x * TILE_SIZE,
                y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ])
        image = pygame.transform.scale(image, (TILE_SIZE * SCALE_FACTOR, TILE_SIZE * SCALE_FACTOR))
        tiles.append(image)
    return tiles

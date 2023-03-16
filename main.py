import pygame

from Character import Character
from constants import TILE_SIZE, SCALE_FACTOR, directions
from MapGenerator import MapGenerator

pygame.init()

WINDOW_WIDTH = TILE_SIZE * SCALE_FACTOR * 5
WINDOW_HEIGHT = TILE_SIZE * SCALE_FACTOR * 5
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

dungeon = MapGenerator(1)
character = Character(1, 1)
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            direction = ""
            if event.key == pygame.K_w:
                direction = "up"
            if event.key == pygame.K_s:
                direction = "down"
            if event.key == pygame.K_a:
                direction = "left"
            if event.key == pygame.K_d:
                direction = "right"
            if direction:
                if dungeon.checkGlobalMove(character.x, character.y, direction):
                    character.move(direction)
    dungeon.displayChunk(screen, character.x, character.y)
    character.display(screen, dungeon.chunkCords)
    pygame.display.update()

pygame.quit()

import pygame

from Character import Character
from constants import TILE_SIZE, SCALE_FACTOR
from MapEngine import MapEngine

pygame.init()

WINDOW_WIDTH = TILE_SIZE * SCALE_FACTOR * 5
WINDOW_HEIGHT = TILE_SIZE * SCALE_FACTOR * 5
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

dungeonEngine = MapEngine(1)
dungeon = dungeonEngine.dungeon
startX, startY = dungeon.startingPoint
character = Character(startX, startY)
running = True
while running:
    if not character.hp:
        running = False
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
    if dungeonEngine.checkPosition(character):
        dungeon = dungeonEngine.dungeon
    pygame.display.update()

pygame.quit()

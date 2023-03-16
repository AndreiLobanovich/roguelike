from constants import \
    tilesPaths, \
    mapSymbols, \
    directions, \
    unpassableTileTypes
from Tile import Tile
from utils import getTiles
import pygame


class MapGenerator:
    def __init__(self, lvl):
        tileImgs = {}
        self.tiles = []
        self.chunkCords = 0, 0, 0, 0
        for entity in tilesPaths.keys():
            tileImgs[entity] = getTiles(
                tilesPaths[entity]['path'],
                tilesPaths[entity]['pos'][0],
                tilesPaths[entity]['pos'][1]
            )
        gameMap = [line.replace('\n', '') for line in open(f'maps/{lvl}').readlines()]
        self.width, self.height = len(gameMap[0]), len(gameMap)
        for y, line in enumerate(gameMap):
            self.tiles.append([])
            for x, symbol in enumerate(line):
                tileType = mapSymbols[symbol]
                speciality = symbol if symbol in "xo" else None
                self.tiles[-1].append(Tile(tileImgs[tileType], tileType, speciality))

    def displayChunk(self, screen, x, y):
        for i, row in enumerate(self.getChunk(x, y)):
            for j, tile in enumerate(row):
                tile.display(screen, j, i)

    def getChunk(self, x, y):
        left, up, right, down = x <= 2, y <= 2, x >= self.width - 3, y >= self.height - 3
        startX, endX, startY, endY = x - 2, x + 3, y - 2, y + 3
        if left:
            startX = 0
            endX = 5
        if up:
            startY = 0
            endY = 5
        if right:
            startX = self.width - 5
            endX = self.width
        if down:
            startY = self.height - 5
            endY = self.height
        self.chunkCords = (startX, endX, startY, endY)
        return [row[startX: endX] for row in self.tiles[startY: endY]]

    def checkGlobalMove(self, x, y, direction):
        x, y = x + directions[direction][0], y + directions[direction][1]
        if not (self.tiles[y][x].tileType in unpassableTileTypes):
            print('true')
            return True
        print('falsew')
        return False

TILE_SIZE = 16
SCALE_FACTOR = 5

directions = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
    "none": (0, 0)
}

unpassableTileTypes = ["wall", "chest"]

tilesPaths = {
    "chest": {
        "path": ["tiles/Chest0.png", "tiles/Chest1.png"],
        "pos": (2, 1)
    },
    "floor": {
        "path": ["tiles/Floor.png"],
        "pos": (2, 8)
    },
    "trap": {
        "path": ["tiles/Trap0.png", "tiles/Trap1.png"],
        "pos": (1, 3)
    },
    "wall": {
        "path": ["tiles/Wall.png"],
        "pos": (2, 8)
    }
}

playerTile = {
    "path": ["tiles/Player0.png", "tiles/Player1.png"],
    "pos": (2, 1)
}

mapSymbols = {
    "#": "wall",
    " ": "floor",
    "t": "trap",
    "c": "chest",
    "o": "floor",
    "x": "floor",
    "e": "floor"
}
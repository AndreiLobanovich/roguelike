from Map import Map


class MapEngine:
    def __init__(self, lvl):
        self.dungeon = Map(lvl)
        self.lvl = lvl

    def checkPosition(self, character):
        if self.dungeon.tiles[character.y][character.x].speciality == 'exit':
            self.nextLvl(character)
            return True
        if self.dungeon.tiles[character.y][character.x].tileType == 'trap':
            if self.dungeon.tiles[character.y][character.x].hit():
                character.hp -= 1
        return False

    def nextLvl(self, character):
        self.lvl += 1
        self.dungeon = Map(self.lvl)
        character.setPosition(self.dungeon.startingPoint)

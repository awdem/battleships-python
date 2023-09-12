from lib.player import Player

class Game:
    def __init__(self):
        self.player = Player()

    def has_unplaced_ships(self):
        for ship in self.player.board.ships:
            if ship.orientation == None:
                return True
        return False

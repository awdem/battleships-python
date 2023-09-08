from lib.ship import Ship
from lib.board import Board
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self):
        self.ships_placed = []
        self.unplaced_ships =  [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        self.board = Board()

    def place_ship(self, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        self.ships_placed.append(ship_placement)
        for ship in self.unplaced_ships:
            if ship.length == length:
                self.unplaced_ships.remove(ship)

    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False

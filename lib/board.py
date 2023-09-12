from lib.ship import Ship

class Board:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.ships =  [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        
    def ship_at(self, row, col):
        for ship in self.ships:
            if ship.covers(row, col):
                return True
        return False

    def place_ship(self, length, orientation, row, col):
        for ship in self.ships:
            if length == ship.length and ship.orientation == None:
                ship.orientation = orientation
                ship.row = row
                ship.col = col
                break
    
    def unplaced_ships(self):
        unplaced_ships_list = [ship for ship in self.ships if ship.orientation == None]
        return unplaced_ships_list
from lib.board_formatter import BoardFormatter

class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game
        self.formatter = BoardFormatter()

    def run(self):
        self._welcome()
        while self.game.has_unplaced_ships():
            self._place_ships()

    def _show(self, message):
        self.io.write(message + "\n")
        
    def _welcome(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")   

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _place_ships(self):
        self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message()))
        self._prompt_for_ship_placement()
        self._show("This is your board now:")
        self._show(self.formatter.format(self.game.player.board))

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.player.board.unplaced_ships()]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")
        self._show("OK.")
        self.game.player.board.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )


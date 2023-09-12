from lib.game import Game

"""
Initialises with a player
"""
def test_initialises_with_a_player():
    game = Game()
    assert hasattr(game, 'player')
    
"""
When the player no placed ships
Then it returns true
"""

def test_when_player_has_no_placed_ships_it_returns_true():
    game = Game()
    assert game.has_unplaced_ships() == True


"""
When the player has placed all ships
Then it returns false
"""

def test_when_player_has_placed_all_ships_it_returns_false():
    game = Game()
    player = game.player
    position = 0

    for ship in player.board.ships:
        position += 1
        ship.orientation = 'vertical'
        ship.row = position
        ship.col = position
    
    assert game.has_unplaced_ships() == False

"""
When the player has a mix of placed and unplaced ships
Then it returns true
"""

def test_when_player_has_placed_some_ships_it_returns_false():
    game = Game()
    player = game.player
    position = 0

    player.board.place_ship(2, 'vertical', 1, 1)
    player.board.place_ship(3, 'vertical', 4, 4)

    assert game.has_unplaced_ships() == True
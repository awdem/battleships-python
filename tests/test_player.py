from lib.player import Player

"""
Initializes with an empty board
"""
def test_initializes_with_an_empty_board():
    player = Player()
    player_board = player.board
    
    for row in range(1, 11):
        for col in range(1, 11):
            assert not player_board.ship_at(row, col)

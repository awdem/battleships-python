from lib.board import Board

"""
Initializes with a length and width of 10
"""

def test_initializes_with_a_length_and_width_of_10():
    board = Board()
    assert board.rows == 10
    assert board.cols == 10
    
"""
Initialises with five unplaced ships of length 2, 3, 3, 4, 5
"""

def test_initialises_with_five_ships_of_right_length():
    board = Board()
    ships = board.ships
    assert len(ships) == 5
    assert ships[0].length == 2 and ships[0].orientation == None
    assert ships[1].length == 3 and ships[1].orientation == None
    assert ships[2].length == 3 and ships[2].orientation == None
    assert ships[3].length == 4 and ships[3].orientation == None
    assert ships[4].length == 5 and ships[4].orientation == None
    
"""
Initialises with a totally empty board
"""

def test_initialises_with_a_totally_empty_board():
    board = Board()
    for row in range(1, 11):
        for col in range(1, 11):
            assert not board.ship_at(row, col)


"""
When we place a ship of unique length
Then parameters are changed to match the placement
"""

def test_when_we_place_a_ship_of_unique_length_then_its_parameters_change():
    board = Board()
    board.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert board.ships[0].orientation == "vertical"
    assert board.ships[0].row == 3
    assert board.ships[0].col == 2

"""
When we place a ship of duplicate length
Only the first unplaced ship of duplicate length is placed
"""

def test_when_we_place_a_ship_of_duplicate_length_then_its_parameters_change():
    board = Board()
    board.place_ship(length=3, orientation="vertical", row=3, col=2)
    assert board.ships[1].orientation == "vertical"
    assert board.ships[2].orientation == None


"""
When we place a ship
Then its place on the board is marked out
"""

def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    board = Board()
    board.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert board.ship_at(3, 2)
    assert board.ship_at(4, 2)
    assert not board.ship_at(3, 3)
    assert not board.ship_at(4, 3)
    assert not board.ship_at(3, 1)
    assert not board.ship_at(4, 1)
    
    
"""
Returns a list of unplaced ships
"""

def test_returns_a_list_unplaced_ships():
    board = Board()

    assert len(board.unplaced_ships()) == 5

    
"""
When soe ships are placed
Returns a list of only the unplaced
"""

def test_returns_a_list_unplaced_ships():
    board = Board()
    
    board.place_ship(length=2, orientation="vertical", row=3, col=2)
    board.place_ship(length=5, orientation="vertical", row=3, col=2)

    assert len(board.unplaced_ships()) == 3

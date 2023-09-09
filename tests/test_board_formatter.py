from lib.board import Board
from lib.board_formatter import BoardFormatter

"""
It initializes
"""

def test_it_initializes():
    formatter = BoardFormatter()
    assert isinstance(formatter, BoardFormatter)

"""
Correctly formats an empty board
"""

def test_correctly_formats_an_empty_board():
    formatter = BoardFormatter()
    board = Board()
    expected_format = "\n".join([
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ])
    
    assert formatter.format(board) == expected_format

"""
Correctly formats an a board with one ship
"""

def test_correctly_formats_an_board_with_one_ship():
    formatter = BoardFormatter()
    board = Board()
    board.place_ship(2, "vertical", 4, 1)
    expected_format = "\n".join([
            "..........",
            "..........",
            "..........",
            "S.........",
            "S.........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ])
    
    assert formatter.format(board) == expected_format

"""
Correctly formats an a board with multiple ships
"""

def test_correctly_formats_an_board_with_multiple_ships():
    formatter = BoardFormatter()
    board = Board()
    board.place_ship(2, "vertical", 4, 1)
    board.place_ship(3, "horizontal", 1, 1)
    board.place_ship(5, "vertical", 1, 10)
    expected_format = "\n".join([
            "SSS......S",
            ".........S",
            ".........S",
            "S........S",
            "S........S",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ])
    
    assert formatter.format(board) == expected_format

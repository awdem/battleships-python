from lib.board import Board

"""
Initializes with a length and width of 10
"""

def test_initializes_with_a_length_and_width_of_10():
    board = Board()
    assert board.rows == 10
    assert board.cols == 10
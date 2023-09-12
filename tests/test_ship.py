import pytest

from lib.ship import Ship

"""
Initialises with a given length, and has orientation, row and col params that default to None
"""

def test_initialises_with_a_given_length():
    ship = Ship(length=5)
    assert ship.length == 5
    assert ship.orientation == None
    assert ship.row == None
    assert ship.col == None

"""
Orientation, row, and col parameters can be passed
"""
def test_initialises_with_a_length_orientation_row_and_col():
    ship = Ship(
        length=5, orientation="vertical", row=3, col=2)
    assert ship.length == 5
    assert ship.orientation == "vertical"
    assert ship.row == 3
    assert ship.col == 2


"""
Checks if vertical ships cover a given row and col
"""
def test_checks_if_vertical_ships_cover_a_given_row_and_col():
    ship = Ship(
        length=5, orientation="vertical", row=3, col=2)
    assert ship.covers(3, 2)
    assert ship.covers(4, 2)
    assert ship.covers(5, 2)
    assert ship.covers(6, 2)
    assert ship.covers(7, 2)
    assert not ship.covers(2, 2)
    assert not ship.covers(8, 2)
    assert not ship.covers(3, 1)
    assert not ship.covers(3, 3)


"""
Checks if horizontal ships cover a given row and col
"""
def test_checks_if_horizontal_ships_cover_a_given_row_and_col():
    ship = Ship(
        length=5, orientation="horizontal", row=3, col=2)
    assert ship.covers(3, 2)
    assert ship.covers(3, 3)
    assert ship.covers(3, 4)
    assert ship.covers(3, 5)
    assert ship.covers(3, 6)
    assert not ship.covers(3, 1)
    assert not ship.covers(3, 7)
    assert not ship.covers(2, 2)
    assert not ship.covers(4, 2)


"""
Has a friendly string representation
"""
def test_has_a_friendly_string_representation():
    ship = Ship(
        length=5, orientation="horizontal", row=3, col=2)
    assert str(
        ship) == "Ship(length=5, orientation=horizontal, row=3, col=2)"

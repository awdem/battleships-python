import unittest
import pytest
from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        
        expected_interactions = [
            ("Welcome to the game!", None),
            ("Set up your ships first.", None),
            ("You have these ships remaining: 2, 3, 3, 4, 5", None),
            ("Which do you wish to place?", "2"),
            ("Vertical or horizontal? [vh]", "v"),
            ("Which row?", "5"),
            ("Which column?", "1"),
            ("OK.", None),
            ("This is your board now:", None),
            ("\n".join([
            "..........",
            "..........",
            "..........",
            "..........",
            "S.........",
            "S.........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]), None),
            ("You have these ships remaining: 3, 3, 4, 5", None),
            ("Which do you wish to place?", "3"),
            ("Vertical or horizontal? [vh]", "v"),
            ("Which row?", "5"),
            ("Which column?", "2"),
            ("OK.", None),
            ("This is your board now:", None),
            ("\n".join([
            "..........",
            "..........",
            "..........",
            "..........",
            "SS........",
            "SS........",
            ".S........",
            "..........",
            "..........",
            ".........."
            ]), None),
            ("You have these ships remaining: 3, 4, 5", None),
            ("Which do you wish to place?", "3"),
            ("Vertical or horizontal? [vh]", "h"),
            ("Which row?", "1"),
            ("Which column?", "1"),
            ("OK.", None),
            ("This is your board now:", None),
            ("\n".join([
            "SSS.......",
            "..........",
            "..........",
            "..........",
            "SS........",
            "SS........",
            ".S........",
            "..........",
            "..........",
            ".........."
            ]), None),
            ("You have these ships remaining: 4, 5", None),
            ("Which do you wish to place?", "4"),
            ("Vertical or horizontal? [vh]", "v"),
            ("Which row?", "5"),
            ("Which column?", "3"),
            ("OK.", None),
            ("This is your board now:", None),
            ("\n".join([
            "SSS.......",
            "..........",
            "..........",
            "..........",
            "SSS.......",
            "SSS.......",
            ".SS.......",
            "..S.......",
            "..........",
            ".........."
            ]), None),
            ("You have these ships remaining: 5", None),
            ("Which do you wish to place?", "5"),
            ("Vertical or horizontal? [vh]", "h"),
            ("Which row?", "2"),
            ("Which column?", "2"),
            ("OK.", None),
            ("This is your board now:", None),
            ("\n".join([
            "SSS.......",
            ".SSSSS....",
            "..........",
            "..........",
            "SSS.......",
            "SSS.......",
            ".SS.......",
            "..S.......",
            "..........",
            ".........."
            ]), None),
        ]
        
        for interaction, user_input in expected_interactions:
            io.expect_print(interaction)
            if user_input:
                io.provide(user_input)
        
        interface.run()  

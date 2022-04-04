from .board import Board
from ..helper_functions import is_jump, get_surrounding_coords


class Game:
    """A class used to represent a Game

    An instance should be created when the game starts, and only one
    instance should be created.

    Attributes
    ----------
    board : Board
        The Board that holds all of the Tile objects
    current_player : int
        Shows whose turn it is, eg. Player 1's turn -> current_player=1
    """

    def __init__(self):
        self.board = Board()
        self.current_player = 1
        self.prev_move = {}


    def check_move(self, start_coords, end_coords, player):
        """A method to check if a movement between two coordinates is a
        valid Hexxagon move

        Parameters
        ----------
        start_coords : list
            3 ints that represent q, r, and s coordinates. This is the
            move's starting point
        end_coords : list
            3 ints that represent q, r, and s coordinates. This is the
            move's ending point
        Returns
        -------
        bool
            True if movement is valid, False otherwise
        """
        q1, r1, s1 = start_coords
        q2, r2, s2 = end_coords

        start_state = self.board.get_state(start_coords)
        end_state = self.board.get_state(end_coords)

        conditions = [
            start_state == player,
            end_state == 0,
            abs(q1 - q2) < 3,
            abs(r1 - r2) < 3,
            abs(s1 - s2) < 3
        ]

        return all(conditions)


    def make_turn(self, start_coords, end_coords):
        """Facilitates a player turn

        If the move is not a jump, this method will create a copy game
        piece on the start coordinates.

        Parameters
        ----------
        start_coords : list
            3 ints that represent q, r, and s coordinates. This is the
            move's starting point
        end_coords : list
            3 ints that represent q, r, and s coordinates. This is the
            move's ending point
        """
        if not self.check_move(start_coords, end_coords, self.current_player):
            raise Exception("Invalid move!")

        self.prev_move["start_coords"] = start_coords
        self.prev_move["end_coords"] = end_coords

        start_tile = self.board.get_tile(start_coords)
        end_tile = self.board.get_tile(end_coords)

        end_tile.state = self.current_player

        if is_jump(start_coords, end_coords):
            start_tile.state = 0

        for coords in get_surrounding_coords(end_coords, self.board):
            tile = self.board.get_tile(coords)

            if tile.state != 0:
                tile.state = self.current_player

        self.current_player = 1 if self.current_player==2 else 2


    def get_state(self, coords):
        """Returns state of Tile at coords"""
        return self.board.get_state(coords)

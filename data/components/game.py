from .board import Board


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


    def check_move(self, start_coords, end_coords):
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
        pass


    def is_jump(self, start_coords, end_coords):
        """A method to check if a movement between two coordinates is a
        jump

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
            True if movement is a jump, False otherwise
        """
        pass


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
        pass

import random

from .tile import Tile


class Board:
    """A class used to represent a game Board

    Attributes
    ----------
    board : dict
        This dictionary contains string keys that represent coordinates
        and Tile values that represent the Tile at the key coordinate
    """

    def __init__(self):
        self.board = {}
        self.starting_tiles = ()


    def __get_key(self, coords):
        """Converts a set of coordinates to its key equivalent

        This method exists so that self.board.keys() can be searched.

        Returns
        -------
        str
            This string can be used to search self.board.keys()
        """
        return f"{coords[0]}, {coords[1]}, {coords[2]}"


    def create_board(self):
        """Populates the self.board attribute with starting Tiles"""
        for q in range(-4, 5):
            for r in range(-4, 5):
                for s in range(-4, 5):
                    if abs(q) + abs(r) + abs(s) <= 8 and s == -q-r:
                        key = self.__get_key([q, r, s])
                        self.board[key] = Tile([q, r, s])

        all_keys = list(self.board.keys())

        p1_starting_keys = []
        p2_starting_keys = []

        for i in range(6):
            k = random.choice(all_keys)
            all_keys.remove(k)

            self.board[k].state = i//3 + 1

            if i//3 == 0:
                p1_starting_keys.append(k)
            else:
                p2_starting_keys.append(k)

        self.starting_tiles = (p1_starting_keys, p2_starting_keys)


    def get_state(self, coords):
        """Returns the state of the Tile at the coordinate

        Parameters
        ----------
        coords : list
            3 ints that represent q, r, and s coordinates
        Returns
        -------
        int
            The state, where 0=empty, 1=Player 1, 2=Player 2
        """
        key = self.__get_key(coords)
        return self.board[key].state


    def get_tile(self, coords):
        """Returns the Tile at the coordinate

        Parameters
        ----------
        coords : list
            3 ints that represent q, r, and s coordinates
        Returns
        -------
        Tile
            Tile at the coordinate
        """
        key = self.__get_key(coords)
        return self.board[key]


    def is_tile(self, coords):
        """Returns whether a Tile exists

        Parameters
        ----------
        coords : list
            3 ints that represent q, r, and s coordinates
        Returns
        -------
        bool
            True if a Tile exists at the given coords, False otherwise
        """
        key = self.__get_key(coords)
        return key in self.board.keys()


    def evaluate(self):
        """Evaluates the current position of the board

        The evaluation is dependent on the gems on boards, where every
        Player 1 gem is +1 towards the evaluation score, and vice versa
        for Player 2.

        Returns
        -------
        int
            Evaluation of the game
        """
        evaluation = 0

        for t in self.board.values():
            if t.state == 1:
                evaluation += 1
            elif t.state == 2:
                evaluation -= 1

        return evaluation


    def is_game_over(self):
        """Checks if the game is finished

        One of the two must be true:
            1) A player has 0 gems on the board
            2) The board is completely full with gems

        Returns
        -------
        boolean
            True if at least one of the conditions above is met, False
            otherwise
        """
        p1_lost = True
        p2_lost = True
        board_is_full = True

        for t in self.board.values():
            if t.state == 1:
                p1_lost = False
            elif t.state == 2:
                p2_lost = False
            else:
                board_is_full = False

        return any([p1_lost, p2_lost, board_is_full])

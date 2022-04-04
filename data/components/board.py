from .tile import Tile


class Board:
    """A class used to represent a game Board

    This is a Singleton class.

    Attributes
    ----------
    board : dict
        This dictionary contains string keys that represent coordinates
        and Tile values that represent the Tile at the key coordinate
    """

    def __init__(self):
        self.board = {}
        self.create_board()


    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Board, cls).__new__(cls)
        return cls.instance


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
                    if abs(q) + abs(r) + abs(s) <= 8:
                        key = self.__get_key([q, r, s])
                        self.board[key] = Tile([q, r, s])

        self.board["0, -3, 3"].state = 1
        self.board["3, 0, -3"].state = 1
        self.board["-3, 3, 0"].state = 1

        self.board["3, -3, 0"].state = 2
        self.board["0, 3, -3"].state = 2
        self.board["-3, 0, 3"].state = 2


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

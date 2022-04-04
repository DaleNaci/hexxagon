class Tile:
    """A class used to represent a tile

    All instances should be created when the game is loaded/started.

    Attributes
    ----------
    q : int
        The q-coordinate of the tile
    r : int
        The r-coordinate of the tile
    s : int
        The s-coordinate of the tile
    state : int
        0 if the tile is empty, 1 if it is owned by player 1, and 2 if
        it is owned by player 2
    """

    def __init__(self, coords, state=0):
        """
        Parameters
        ----------
        coords : list
            3 ints that represent q, r, and s coordinates
        state : int
            0 if the tile is empty, 1 if it is owned by player 1, and 2 if
            it is owned by player 2
        """
        self.q = coords[0]
        self.r = coords[1]
        self.s = coords[2]
        self.state = state


    def __str__(self):
        """Converts an instance to a info string

        To run this method, use the built-in str() function on an
        instance.

        Returns
        -------
        info : str
            A multi-line string with information about a Tile instance.
        """
        info = f"q: {self.q}\n" \
                + f"r: {self.r}\n" \
                + f"s: {self.s}\n" \
                + f"state: {self.state}"
        return info

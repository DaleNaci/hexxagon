from .tile import Tile


class Board:
    def __init__(self):
        self.board = {}
        create_board()


    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Board, cls).__new__(cls)
        return cls.instance


    def __get_key(self, coords):
        return f"{coords[0]}, {coords[1]}, {coords[2]}"


    def create_board(self):
        for q in range(-4, 5):
            for r in range(-4, 5):
                for s in range(-4, 5):
                    if abs(q) + abs(r) + abs(s) <= 8:
                        key = self.__get_key([q, r, s])
                        self.board[key] = Tile([q, r, s])


    def get_state(self, coords):
        key = self.__get_key(coords)
        return self.board[key].state


    def get_tile(self, coords):
        key = self.__get_key(coords)
        return self.board[key]


    def is_tile(self, coords):
        key = self.__get_key(coords)
        return key in self.board.keys()

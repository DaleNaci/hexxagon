from .tile import Tile


class Board:
    def __init__(self):
        self.board = {}
        create_board()


    def __get_key(self, coords):
        return f"{coords[0]}, {coords[1]}, {coords[2]}"


    def create_board(self):
        for q in range(-3, 4):
            for r in range(-3, 4):
                for s in range(-3, 4):
                    if abs(q) + abs(r) + abs(s) <= 6:
                        key = self.__get_key([q, r, s])
                        self.board[key] = Tile([q, r, s])


    def get_state(self, q, r, s):
        key = self.__get_key([q, r, s])
        return self.board[key].state

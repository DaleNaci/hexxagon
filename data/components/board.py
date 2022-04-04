from tile import Tile


class Board:
    def __init__(self):
        self.board = {}
        create_board()


    def __get_key(self, q, r, s):
        return f"{q}, {r}, {s}"


    def create_board(self):
        for q in range(3):
            for r in range(3):
                for s in range(3):
                    if abs(q) + abs(r) + abs(s) <= 6:
                        key = self.__get_key(q, r, s)

                        self.board[key] = Tile(q, r, s)


    def get_state(self, q, r, s):
        key = self.__get_key(q, r, s)
        return self.board[key].state

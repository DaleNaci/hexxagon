from copy import deepcopy

from .game import Game
from ..helper_functions import get_surrounding_coords


class Ai:
    def __init__(self, player_num, initial_depth=3):
        self.initial_depth = initial_depth
        self.player_num = player_num

        self.oppo_num = 1 if player_num==2 else 2


    def find_best_move(self, game):
        start_coords = None
        end_coords = None
        max_eval = -9999
        
        for child in self.child_games(game, self.player_num):
            eval = self.minimax(child, self.initial_depth-1, False)

            if eval > max_eval:
                max_eval = eval

                start_coords = child.prev_move["start_coords"]
                end_coords = child.prev_move["end_coords"]

        return (max_eval, start_coords, end_coords)


    def minimax(self, game, depth, maximizing_player):
        if depth == 0 or game.board.is_game_over():
            return game.board.evaluate()

        if maximizing_player:
            max_eval = -9999

            for child in self.child_games(game, self.player_num):
                eval = self.minimax(child, depth-1, False)

                if max_eval < eval:
                    max_eval = eval

            return max_eval

        else:
            min_eval = 9999

            for child in self.child_games(game, self.oppo_num):
                eval = self.minimax(child, depth-1, True)

                if min_eval > eval:
                    min_eval = eval

            return min_eval


    def child_games(self, game, player):
        games = []

        for t in game.board.board.values():
            if t.state == player:
                start_coords = [t.q, t.r, t.s]

                for coords in get_surrounding_coords(start_coords, game.board):
                    if game.board.get_state(coords) == 0:
                        new_game = deepcopy(game)
                        new_game.make_turn(start_coords, coords)

                        games.append(new_game)

        return games

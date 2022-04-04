import random
from copy import deepcopy

from ..components.game import Game
from ..helper_functions import get_surrounding_coords


class Randomizer:
    def __init__(self, player_num):
        self.player_num = player_num


    def pick_random_move(self, game):
        games = self.child_games(game, self.player_num)

        game_picked = random.choice(games)

        start_coords = game_picked.prev_move["start_coords"]
        end_coords = game_picked.prev_move["end_coords"]

        return (start_coords, end_coords)


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

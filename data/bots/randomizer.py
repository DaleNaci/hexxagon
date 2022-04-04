import random
from copy import deepcopy

from ..components.game import Game
from ..helper_functions import get_surrounding_coords


class Randomizer:
    """An AI that just randomly picks moves for every turn

    Attributes
    ----------
    player_num : int
        1 if first player, 2 if second player
    """

    def __init__(self, player_num):
        self.player_num = player_num


    def pick_random_move(self, game):
        """Picks a random next move out of all possible moves

        Parameters
        ----------
        game : Game
            Current game state

        Returns
        -------
        tuple
            [0] -> Starting coordinates
            [1] -> Ending coordinates
        """
        games = self.child_games(game, self.player_num)

        game_picked = random.choice(games)

        start_coords = game_picked.prev_move["start_coords"]
        end_coords = game_picked.prev_move["end_coords"]

        return (start_coords, end_coords)


    def child_games(self, game, player):
        """Gives all the possible game states after one move

        Parameters
        ----------
        game : Game
            The game state that this function creates future states of
        player : int
            Tells the code whose turn it is

        Returns
        -------
        list
            List of all possible game states after one move
        """
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

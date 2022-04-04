import turtle

from .components.game import Game
from .ui_components.turtle_functions import *


def main():
    game = Game()
    game.board.create_board()

    wn = turtle.Screen()
    wn.tracer(0)

    t = turtle.Turtle()
    draw_board(t, game)
    draw_pieces(wn, game)

    wn.update()

    while True:
        print(f"\nPlayer {game.current_player}:")

        start_coords = list(map(int, input("\tStarting Coords: ").split()))
        end_coords = list(map(int, input("\tEnding Coords: ").split()))

        if game.check_move(start_coords, end_coords, game.current_player):
            game.make_turn(start_coords, end_coords)

            draw_pieces(wn, game)

            wn.update()
        else:
            print("Invalid move! Try again!\n")




    # game.make_turn([4, -4, 0], [3, -4, 1])
    # game.make_turn([4, 0, -4], [4, -1, -3])
    #
    # game.make_turn([3, -4, 1], [1, -4, 3])
    # game.make_turn([4, -1, -3], [4, -2, -2])
    #
    # game.make_turn([4, -4, 0], [4, -3, -1])
    # game.make_turn([4, -1, -3], [3, -2, -1])

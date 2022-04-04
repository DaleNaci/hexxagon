import turtle
import time

from .components.game import Game
from .components.ai import Ai
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

    p1 = Ai(1, 1)
    p2 = Ai(2, 3)

    # game.make_turn([4, -4, 0], [3, -4, 1])
    # game.make_turn([4, 0, -4], [4, -1, -3])
    #
    # game.make_turn([3, -4, 1], [1, -4, 3])
    # game.make_turn([4, -1, -3], [4, -2, -2])
    #
    # game.make_turn([4, -4, 0], [4, -3, -1])
    # game.make_turn([4, -1, -3], [3, -2, -1])
    #
    # print(p1.find_best_move(game))
    #
    # draw_pieces(wn, game)
    # wn.update()
    #
    # wn.mainloop()

    while True:
        print(f"\nPlayer {game.current_player}:")

        if game.current_player == 1:
            eval, start_coords, end_coords = p1.find_best_move(game)
            print(eval)

            try:
                game.make_turn(start_coords, end_coords)
            except:
                print("Player 2 wins.")
                break
        else:
            # start_coords = list(map(int, input("\tStarting Coords: ").split()))
            # end_coords = list(map(int, input("\tEnding Coords: ").split()))
            #
            # if game.check_move(start_coords, end_coords, game.current_player):
            #     game.make_turn(start_coords, end_coords)
            # else:
            #     print("Invalid move! Try again!\n")
            #     continue
            eval, start_coords, end_coords = p2.find_best_move(game)
            print(eval)
            try:
                game.make_turn(start_coords, end_coords)
            except:
                input()
                print("Player 1 wins.")
                break

        draw_pieces(wn, game)
        wn.update()

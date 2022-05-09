import turtle
import time

from .components.game import Game
from .components.ai import Ai
from .ui_components.turtle_functions import *
from .bots.randomizer import Randomizer
from .helper_functions import is_jump


RUN_UI = False

def main(scenario=1):
    """This is the main function

    It contains every single game loop and puts together all of the
    different components.

    Parameters
    ----------
    scenario : int
        Every single number will run the game in a different way
    """
    # game = Game()
    # game.board.create_board()

    if RUN_UI:
        wn = turtle.Screen()
        wn.tracer(0)

        t = turtle.Turtle()
        t.hideturtle()

        draw_board(t, game)
        draw_pieces(wn, game)

        wn.update()

    # MINIMAX VS. MINIMAX
    if scenario == 1:
        for i in range(1000):
            MOVE_COUNT = 0
            p1_jumps = 0
            p2_jumps = 0
            RESULT = ""

            print(f"Game {i+1}")
            game = Game()
            game.board.create_board()

            p1 = Ai(1, 2)
            p2 = Ai(2, 2)

            while True:
                MOVE_COUNT += 1
                if MOVE_COUNT > 200:
                    RESULT = "Tie"
                    break

                if game.current_player == 1:
                    eval, start_coords, end_coords = p1.find_best_move(game)

                    try:
                        game.make_turn(start_coords, end_coords)

                        if is_jump(start_coords, end_coords):
                            p1_jumps += 1
                    except:
                        RESULT = "Loss"
                        break
                else:
                    eval, start_coords, end_coords = p2.find_best_move(game)

                    try:
                        game.make_turn(start_coords, end_coords)

                        if is_jump(start_coords, end_coords):
                            p2_jumps += 1
                    except:
                        RESULT = "Win"
                        break

                if RUN_UI:
                    draw_pieces(wn, game)
                    wn.update()

            p1_score, p2_score = game.get_scores()
            p1_starting_tiles, p2_starting_tiles = game.board.starting_tiles

            p1_s = []
            p2_s = []

            for s in p1_starting_tiles:
                p1_s.append(s.replace(",", ""))

            for s in p2_starting_tiles:
                p2_s.append(s.replace(",", ""))

            with open("output.csv", "a") as f:
                f.write(f"{i+1},{MOVE_COUNT},{p1_score},{p2_score},{RESULT},{p1_jumps},{p2_jumps},{p1_s[0]},{p1_s[1]},{p1_s[2]},{p2_s[0]},{p2_s[1]},{p2_s[2]}\n")


    # MINIMAX VS PLAYER
    elif scenario == 2:
        p1 = Ai(1, 1)

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
                start_coords = list(map(int, input("\tStarting Coords: ").split()))
                end_coords = list(map(int, input("\tEnding Coords: ").split()))

                if game.check_move(start_coords, end_coords, game.current_player):
                    game.make_turn(start_coords, end_coords)
                else:
                    print("Invalid move! Try again!\n")
                    continue

            draw_pieces(wn, game)
            wn.update()

    # MINIMAX vs. RANDOM
    elif scenario == 3:
        p1 = Ai(1, 3)
        p2 = Randomizer(2)

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
                try:
                    start_coords, end_coords = p2.pick_random_move(game)
                    game.make_turn(start_coords, end_coords)
                except:
                    input()
                    print("Player 1 wins.")
                    break

            draw_pieces(wn, game)
            wn.update()

    # MINIMAX vs. MINIMAX Pre-determined board
    elif scenario == 4:
        game.make_turn([4, -4, 0], [3, -4, 1])
        game.make_turn([4, 0, -4], [4, -1, -3])

        game.make_turn([3, -4, 1], [1, -4, 3])
        game.make_turn([4, -1, -3], [4, -2, -2])

        game.make_turn([4, -4, 0], [4, -3, -1])
        game.make_turn([4, -1, -3], [3, -2, -1])

        p1 = Ai(1, 3)
        p2 = Ai(2, 3)

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

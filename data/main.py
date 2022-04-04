import turtle

from .components.game import Game


def draw_hex(t):
    for i in range(6):
        t.forward(60)
        t.left(60)


def row_of_hexes(t, n):
    for i in range(n-1):
        draw_hex(t)
        t.up()
        t.forward(60)
        t.right(60)
        t.forward(60)
        t.left(60)
        t.down()
    draw_hex(t)


def snake(t, seq):
    for c in seq:
        if c == "f":
            t.forward(60)
        elif c == "r":
            t.right(60)
        else:
            t.left(60)


def draw_board(t, game):
    t.speed(0)

    t.up()
    t.goto(-30, 350)
    t.down()

    row_of_hexes(t, 5)

    snake(t, "flll")
    row_of_hexes(t, 6)

    snake(t, "flfrflflfl")
    row_of_hexes(t, 7)

    snake(t, "frrr")
    row_of_hexes(t, 8)

    snake(t, "flfrflflfl")
    row_of_hexes(t, 9)

    snake(t, "lllrfl")
    row_of_hexes(t, 8)

    snake(t, "flflfrflfl")
    row_of_hexes(t, 7)

    snake(t, "llfl")
    row_of_hexes(t, 6)

    snake(t, "flflfrflfl")
    row_of_hexes(t, 5)



def main():
    game = Game()
    game.board.create_board()

    wn = turtle.Screen()
    wn.tracer(0)

    t = turtle.Turtle()

    draw_board(t, game)

    wn.update()


    while True:
        print(f"Player {game.current_player}:")

        start_coords = list(map(int, input("\tStarting Coords: ").split()))
        end_coords = list(map(int, input("\tEnding Coords: ").split()))

        if game.check_move(start_coords, end_coords, game.current_player):
            game.make_turn(start_coords, end_coords)
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

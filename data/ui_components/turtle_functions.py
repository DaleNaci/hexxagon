import turtle


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
    t.goto(-30, 365)
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


def draw_pieces(wn, game):
    with open("./resources/coordinate_data/map1.txt") as f:
        for line in f.readlines():
            q, r, s, x, y = line.split()

            key = f"{q}, {r}, {s}"
            tile = game.board.board[key]
            if tile.state == 2:
                a = turtle.Turtle()
                a.up()
                a.shape("circle")
                a.goto(float(x), float(y))
                a.color("blue")
            elif tile.state == 1:
                a = turtle.Turtle()
                a.up()
                a.shape("circle")
                a.goto(float(x), float(y))
                a.color("red")
            else:
                a = turtle.Turtle()
                a.up()
                a.shape("circle")
                a.goto(float(x), float(y))
                a.color("white")

    wn.update()

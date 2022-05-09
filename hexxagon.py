from data.main import main


if __name__ == "__main__":
    """
    Scenarios

    1 -> Minimax vs. Minimax
    2 -> Minimax vs. Player
    3 -> Minimax vs. Randomizer
    4 -> Minimax vs. Minimax on pre-determined board
    """
    main(3)


"""
Sample Player 2 Moves!
[4, 0, -4] -> [4, -1, -3]
[4, -1, -3] -> [4, -2, -2]
[4, -1, -3] -> [3, -2, -1]
"""

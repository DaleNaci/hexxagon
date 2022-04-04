from .components.board import Board


def is_jump(start_coords, end_coords):
    """A method to check if a movement between two coordinates is a
    jump

    Parameters
    ----------
    start_coords : list
        3 ints that represent q, r, and s coordinates. This is the
        move's starting point
    end_coords : list
        3 ints that represent q, r, and s coordinates. This is the
        move's ending point

    Returns
    -------
    bool
        True if movement is a jump, False otherwise
    """
    q1, r1, s1 = start_coords
    q2, r2, s2 = end_coords

    conditions = [
        abs(q1 - q2) == 2,
        abs(r1 - r2) == 2,
        abs(s1 - s2) == 2
    ]

    return any(conditions)


def get_surrounding_coords(coords):
    surrounding_coords = []
    board = Board()

    modifications = [
        [1, 0, -1],
        [1, -1, 0],
        [0, -1, 1],
        [-1, 0, 1],
        [-1, 1, 0],
        [0, 1, -1]
    ]

    for mod in modifications:
        adjacent_coords = [
            coords[0] + mod[0],
            coords[1] + mod[1],
            coords[2] + mod[2]
        ]

        if board.is_tile(adjacent_coords):
            surrounding_coords.append(adjacent_coords)

    return surrounding_coords
from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.

    assert len(input_board) > 0

    for rows in input_board:
        assert len(rows) == len(input_board[0])

    def f_fill(x, y):
        if 0 <= x < len(input_board) and 0 <= y < len(input_board[0]) and input_board[x][y] == old:
            input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
            f_fill(x + 1, y)
            f_fill(x - 1, y)
            f_fill(x, y + 1)
            f_fill(x, y - 1)

    f_fill(x, y)
    return input_board

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

for a in modified_board:
    print(a)

from turtle import pos


positions = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
             ]

# column = input("Choose column: ")
# column = input("Choose row: ")


def player_placement(row, column):
    return positions[row][column]


def board(pos):
    board_pieces = []

    rows = [[f"\t   {'X'} |", f" {'X'} ", f"| {'X'}"],
            [f"\t   {'X'} |", f" {'X'} ", f"| {'X'}"],
            [f"\t   {'X'} |", f" {'X'} ", f"| {'X'}"]]

    # for row in rows:
    print(rows[0][0], rows[0][1], rows[0][2])
    print(f"\t ____|_____|____")
    print(rows[1][0], rows[1][1], rows[1][2])
    print(f"\t ____|_____|____")
    print(rows[2][0], rows[2][1], rows[2][2])
    print(f"\t     |     |   ")


board()

# is_game_on = True

# while is_game_on:
#     pass

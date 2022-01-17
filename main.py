from operator import indexOf


positions = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']
             ]


def board(row, column):

    positions[row][column] = "X"

    pos = [[f"\t   {positions[0][0]}  |", f" {positions[0][1]} ", f"| {positions[0][2]}"],
           [f"\t   {positions[1][0]}  |",
           f" {positions[1][1]} ", f"| {positions[1][2]}"],
           [f"\t   {positions[2][0]}  |",
           f" {positions[2][1]} ", f"| {positions[2][2]}"],
           ]

    print(pos[0][0], pos[0][1], pos[0][2])
    print(f"\t  ____|_____|____")
    print(pos[1][0], pos[1][1], pos[1][2])
    print(f"\t  ____|_____|____")
    print(pos[2][0], pos[2][1], pos[2][2])
    print(f"\t      |     |   ")


is_game_on = True

while is_game_on:
    row = int(input("Choose row: "))
    column = int(input("Choose column: "))
    board(row, column)

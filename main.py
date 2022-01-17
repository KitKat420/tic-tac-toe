turn = True

positions = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']
             ]


def is_game_over():
    """This function checks to see if a player won"""
    row = 0
    column = 0

    while row <= 2:
        if positions[row][0] == "X" and positions[row][1] == "X" and positions[row][2] == "X":
            return False
        elif positions[row][0] == "O" and positions[row][1] == "O" and positions[row][2] == "O":
            return False
        elif positions[0][column] == "X" and positions[1][column] == "X" and positions[2][column] == "X":
            return False
        elif positions[0][column] == "O" and positions[1][column] == "O" and positions[2][column] == "O":
            return False
        elif positions[0][0] == "X" and positions[1][1] == "X" and positions[2][2] == "X":
            return False
        elif positions[0][2] == "O" and positions[1][1] == "O" and positions[2][0] == "O":
            return False
        elif positions[0][0] == "O" and positions[1][1] == "O" and positions[2][2] == "O":
            return False
        elif positions[0][2] == "X" and positions[1][1] == "X" and positions[2][0] == "X":
            return False

        row += 1
        column += 1
    return True


def board(row, column, player, turn):
    """This function maintains the current state of game board"""

    try:
        positions[row][column] = player
    except IndexError:
        print("Invalid position: Please try again.")
    else:
        turn()

    # Position layout
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


def player_turn():
    """This function changes turns"""
    global turn
    global player_shape
    if turn:
        player_shape = "O"
        turn = False
    else:
        player_shape = "X"
        turn = True


player_shape = input("Player #1 choose shape: ")

is_game_on = True

while is_game_on:
    is_game_on = is_game_over()

    if not is_game_on:
        break

    row = int(input("Choose row: "))
    column = int(input("Choose column: "))
    board(row, column, player_shape, player_turn)

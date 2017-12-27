import random

grid = [["-" for _ in xrange(3)] for _ in xrange(3)]
grid_space = 9

player1_name = ""
player2_name = ""

marker1 = "O"
marker2 = "X"

player_turn = ""
game_state = 1 # 1 for in play 2 for finished

def ask_players_name():
    global player1_name
    global player2_name

    p1_name = raw_input("Enter Player 1 Name: ")
    player1_name = p1_name if p1_name != "" else "Joe"

    p2_name = raw_input("Enter Player 2 Name: ")
    player2_name = p2_name if p2_name != "" else "Jane"


def ask_play():
    global player_turn
    print ("It's {0}'s turn to play".format(get_players_name_by_marker(player_turn)))
    handle_coordinate(player_turn)

def handle_coordinate(marker):
    global grid_space

    is_valid = False

    while not is_valid and grid_space > 0:
        n = int(raw_input("X Coordinates: "))
        m = int(raw_input("Y Coordinates: "))

        if not check_input(n, m):
            continue
        if check_empty(n, m):
            print ("Selected Coordinate is not empty")
            continue
        put_marker(m, n, marker)
        grid_space -= 1
        is_valid = True

    if grid_space == 0:
        global game_state
        game_state = 3
        return

def get_players_name_by_marker(marker):
    global player1_name
    global player2_name

    global marker1

    return player1_name if marker == marker1 else player2_name

def change_turn(marker):
    global marker1
    global marker2

    global player_turn

    player_turn = marker2 if marker == marker1 else marker1

def check_input(n, m):
    if n < 0 or n > 2:
        print("Selected Row was not valid")
        return False
    if m < 0 or m > 2:
        print("Selected Column was not valid")
        return False
    return True

def check_empty(n,m):
    global grid
    return grid[n][m] == 0

def check_win_condition(marker):
    global grid
    global game_state

    # Row and Col Check
    for i in xrange(3):
        row = []
        col = []
        for j in xrange(3):
            if grid[i][j] == marker:
                row.append(True)
            else:
                row.append(False)

            if grid[j][i] == marker:
                col.append(True)
            else:
                col.append(False)
        if all(row) or all(col):
            return True

    # Diagonal Check
    diag = []
    reverse_diag = []
    for i in xrange(3):
        if grid[i][i] == marker:
            diag.append(True)
        else:
            diag.append(False)

        if grid[i][2-i] == marker:
            reverse_diag.append(True)
        else:
            reverse_diag.append(False)

    if all(diag) or all(reverse_diag):
        return True

    return False


def put_marker(n, m, marker):
    global grid
    grid[n][m] = marker

def coin_toss():
    return "O" if random.randint(1,2) == 1 else "X"

def handle_initializing():
    global player_turn

    ask_players_name()
    player_turn = coin_toss()

def print_grid():
    global grid
    print("Tic-tac-toe Grid:")
    for i in xrange(3):
        rows = []
        for j in xrange(3):
            rows.append(grid[i][j])
        print ("{0} | {1} | {2}".format(rows[0], rows[1], rows[2]))


def main():
    global game_state
    global player_turn

    print ("Welcome to Tic-Tac-Toe")
    handle_initializing()
    while game_state == 1:
        ask_play()
        print_grid()
        if check_win_condition(player_turn):
            game_state = 2
            break
        change_turn(player_turn)

    if game_state == 2:
        print_grid()
        print ("Player {0} wins!".format(get_players_name_by_marker(player_turn)))

    if game_state == 3:
        print ("It's a draw.")

    exit()

if __name__ == "__main__":
    main()
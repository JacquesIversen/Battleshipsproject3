from random import randint

def main():
    global BOARDSIZE
    BOARDSIZE = 0
    print("gamestart")
    while BOARDSIZE not in range(5, 10):
        BOARDSIZE = input("Enter board size inbetween 5-9: ")
        BOARDSIZE = int(BOARDSIZE)  #Only int from user
    create_board(BOARDSIZE)
    ships(PLAYER_BOARD)
    create_ships()
    enemy_ships()
    ships(HIDDEN_BOARD)


def create_board(size):
    global PLAYER_BOARD, HIDDEN_BOARD
    PLAYER_BOARD = [[" "] * size for x in range(size)]
    HIDDEN_BOARD = [[" "] * size for x in range(size)]


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
}


# Creates a platform multiplied by input
def ships(create_board):
    alphabet = "A B C D E F G H I J"
    print("  " + alphabet[0: (BOARDSIZE*2)]) 
    row_num = 1
    for row in create_board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def create_ships():
    ship_amount = BOARDSIZE * 2
    for ship in range(ship_amount):
        row, column = randint(0, BOARDSIZE-1), randint(0, BOARDSIZE-1) #Index Array
        while HIDDEN_BOARD[row][column] == "X":
            row, column = randint(0, BOARDSIZE-1), randint(0, BOARDSIZE-1) #Index Array
        HIDDEN_BOARD[row][column] = "X"


def enemy_ships():
    row = input("Place a value between 1 & " "insert BOARDSIZE here: ")
    while row not in "123456789":
        print("You were supposed to pick a NUMBER")
        row = input("Now, let's try again. Pick a number between 1 & BOARDSIZE: ")
    column = input("Place a latitude value 'ABC...' ").upper()  #ensures capital letter
    while column not in "ABCDEFGHI":
        print("I though you understood the rules here.. -.-")
        column = input("A letter from A - BOARDSIZE").upper()
    return int(row) - 1, letters_to_numbers[column]



def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

main()
# Execute main function, turns will be inputed number.
"""
if __name__ == "__main__":
    turns = BOARDSIZE
    while turns > 0:
        print("Pick a guess for your strike")
        ships(PLAYER_BOARD)
        """
from random import randint


def main():
    global BOARDSIZE
    BOARDSIZE = 0
    print("Welcome to the unbeatable Battleship Navy")
    while BOARDSIZE not in range(5, 10):
        try: 
            BOARDSIZE = input("Enter board size inbetween 5-9: \n")
            BOARDSIZE = int(BOARDSIZE)  #Only int from user
        except ValueError:
            print("Sorry, please pick a number between 5-9")
    create_board(BOARDSIZE)
    #print_ships(PLAYER_BOARD)
    create_ships()
    #print_ships(HIDDEN_BOARD)
    turns = BOARDSIZE * 3
    while turns > 0:
        print_ships(PLAYER_BOARD)
        row, column = enemy_ships()
        print_ships(HIDDEN_BOARD) #Print enemy board before your shot. 
        if HIDDEN_BOARD[row][column] == "X":
            print("You've sunk my battelship")
            PLAYER_BOARD[row][column] = "X"
            turns -= 1
        elif HIDDEN_BOARD[row][column] == " ":
            print("'Splash' is the sound of a miss....")
            HIDDEN_BOARD[row][column] = "-"
            PLAYER_BOARD[row][column] = "-"
            turns -= 1
        elif HIDDEN_BOARD[row][column] == "-":
            print("Guessed already")
        print("You have", turns, "shots remaining")
        score = count_hit_ships()
        print(BOARDSIZE - score, "more hits to win the game.")
        print("You currently hit", score, "ships")
        if score == BOARDSIZE:
            print("Success, you've sunk the invading Naval Officer")
            break
        if turns == 0:
            print("Sucker, how did you actually manage to lose?")
            break
        if turns < BOARDSIZE - score:
            print("Oh no! You are CheckMate.....")
            break


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
def print_ships(create_board):
    alphabet = "A B C D E F G H I J"
    print("  " + alphabet[0: (BOARDSIZE*2)]) 
    row_num = 1
    for row in create_board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def create_ships():
    global SHIP_AMOUNT
    SHIP_AMOUNT = BOARDSIZE * 2
    for ship in range(SHIP_AMOUNT):
        row, column = randint(0, BOARDSIZE-1), randint(0, BOARDSIZE-1)
        while HIDDEN_BOARD[row][column] == "X":
            row, column = randint(0, BOARDSIZE-1), randint(0, BOARDSIZE-1)
        HIDDEN_BOARD[row][column] = "X"



def enemy_ships():
    alphabet = "ABCDEFGHI"
    numbers = "123456789"
    row = input("Pick a row between 1 & " + str(BOARDSIZE) + ": \n")
    input_empty = row == ""
    while input_empty or row not in numbers[0: BOARDSIZE]:
        print("You were supposed to pick a number between 1 & "+ str(BOARDSIZE))
        row = input("Let's try again. Pick a number between 1 & "+ str(BOARDSIZE) + ": \n")
        if len(row) == 1 and row in numbers[0: BOARDSIZE]:
            input_empty = False
    column = input("Place a latitude letter from A - " + str(alphabet[BOARDSIZE - 1])+ ": \n").upper()
    input_empty = column == ""
    while column not in alphabet[0: BOARDSIZE] or input_empty:
        print("I though you understood the rules here.. -.-")
        column = input("A letter from A - " + str(alphabet[BOARDSIZE - 1])+ " please: \n").upper()
        if len(column) == 1 and column in alphabet[0: BOARDSIZE]:
            input_empty = False
    return int(row) - 1, letters_to_numbers[column]


#check if all ships are hit
def count_hit_ships():
    count = 0
    for row in PLAYER_BOARD:
        for column in row:
            if column == "X":
                count += 1
    return count


# Execute main function, turns will be inputed number.

if __name__ == "__main__":
    main()







"""
if __name__ == "__main__":
    #create_ships(HIDDEN_BOARD)
    create_board(size)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        ships(PLAYER_BOARD)
        row, column = enemy_ships()
        if PLAYER_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            PLAYER_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            PLAYER_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(PLAYER_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
"""
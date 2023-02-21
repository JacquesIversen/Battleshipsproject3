from random import randint

def main():
    global BOARDSIZE
    BOARDSIZE = 0
    print("gamestart")
    while BOARDSIZE not in range(5, 10):
        BOARDSIZE = input("Enter board size inbetween 5-9: ")
        BOARDSIZE = int(BOARDSIZE)
    create_board(BOARDSIZE)
    ships(PLAYER_BOARD)
    create_ships()
    ships(HIDDEN_BOARD)


def create_board(size):
    global PLAYER_BOARD, HIDDEN_BOARD
    PLAYER_BOARD = [[" "] * size for x in range(size)]
    HIDDEN_BOARD = [[" "] * size for x in range(size)]
    

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
        print(row, column)
        while HIDDEN_BOARD[row][column] == "X":
            row, column = randint(0, BOARDSIZE-1), randint(0, BOARDSIZE-1) #Index Array
        HIDDEN_BOARD[row][column] = "X"



"""def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][
"""


# Execute main function
if __name__ == "__main__":
    main()




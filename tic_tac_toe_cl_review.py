
import time 
from random import randrange
import sys

time_delay = 0.75


board = [[1,2,3],[4,5,6],[7,8,9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    board_template = f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
        """
    print(board_template)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    time.sleep(time_delay)
    while True:
        try:
            user_move = int(input('State the number to wish to place your token on: '))
            if user_move > 9 or user_move < 1:
                print("please enter an available number between 1 and 9")
            elif user_move not in free_fields:
                print("please choose an available number")
            else: 
                break
        except KeyboardInterrupt:
            print("Ctrl-C pressed!")
            sys.exit(0)
        except:
            print("Please enter a vaild number")
    update_column = (user_move + 2) % 3
    update_row = (user_move - 1) // 3 
    board[update_row][update_column] = "O"
    time.sleep(time_delay)
    display_board(board)
    victory_for(board, "O")
    

    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in board:
        for square in row:
            if type(square) == int:
                free_fields.append(square)
    if len(free_fields) == 0:
            print("Game is a tie. Game over!")
            sys.exit(0)        
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winning_combinations = [
        [(0,0), (0,1), (0,2)], #top row 
        [(1,0), (1,1), (1,2)], #middle row
        [(2,0), (2,1), (2,2)], #bottom row 
        [(0,0), (1,0), (2,0)], #left column
        [(0,0), (1,1), (2,2)], #ul-lr diagonal
        [(0,1), (1,1), (2,1)], #middle column
        [(0,2), (1,2), (2,2)], #right row 
        [(2,0), (1,1), (0,2)], #ll-ur diagonal row
                                
    ]

    for combo in winning_combinations:
        if all(board[r][c] == sign for r, c, in combo):
            print(f"{sign} wins. Game over")
            sys.exit(0)


    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[2][0] == sign and  board[2][1] == sign and  board[2][2] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[0][0] == sign and  board[1][0] == sign and  board[2][0] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[0][0] == sign and  board[1][1] == sign and  board[2][2] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[0][1] == sign and  board[1][1] == sign and  board[2][1] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[0][2] == sign and  board[1][2] == sign and  board[2][2] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    elif board[2][0] == sign and  board[1][1] == sign and  board[0][2] == sign:
        time.sleep(time_delay)
        print(f"{sign} wins. Game over")
        sys.exit(0)
    else:
        return 


def draw_move(board):
    #The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    #print(f"free fields: {free_fields}")
    random_number = randrange(len(free_fields))
    #print(f"length of free fields list: {len(free_fields)}")
    #print(f"random number chosen: {random_number}")
    computer_choice = free_fields[random_number]
    update_column = (computer_choice + 2) % 3
    update_row = (computer_choice -1 ) // 3 
    board[update_row][update_column] = "X"
    time.sleep(time_delay)
    print("Computer's next move...")
    time.sleep(time_delay)
    print("Thinking....")
    display_board(board)
    victory_for(board, "X")



    
print(" \n \n \n Welcome to Tic Tac Toe..... \n \n \n ")
time.sleep(time_delay)
print("Here's the board: \n")
time.sleep(time_delay)
display_board(board)
time.sleep(time_delay)
print("\n Computer will go first and start with X. You will be O. \n\n\n") 
time.sleep(time_delay)
print("Computers's first move: ")
time.sleep(time_delay)
board = [[1,2,3],[4,"X",6],[7,8,9]]
display_board(board)
while True:
    try:
        enter_move(board)
        draw_move(board)
    except KeyboardInterrupt:
        print("Ctrl-C pressed!")
        sys.exit(0)




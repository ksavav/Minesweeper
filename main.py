#minesweeper

import random
from gameboard import GameBoard

def sweeper():
    used_cords = list()

    win = False
    lose = False

    while win == False and lose == False:
        player_move(used_cords)

def player_move(used_cords):
    while True:
        try:
            user_move = input("make your move. Type the nuber of the column and the number of the row u want to uncover (f.e. 9:2 <- column 9, row 2): \n")
            
            user_move = user_move.split(":")
            pos_x = int(user_move[0])
            pos_y = int(user_move[1])

            used_cord = [pos_x, pos_y]

            if used_cord not in used_cords:
                break
            
            else: print("You used thoes cords already!")

            
        
        except:
            if IndexError: print("Provide only two numbrs, first for the column and second for the row\n")
            elif ValueError: print("You should provide two numbers!\n")

    used_cords.append(used_cord)



if __name__ == "__main__":
    board = GameBoard()

    full_board = board.creat_board(30, 10) #columns, rows

    board.creat_numbers_of_mines(full_board)

    board.print_board(full_board)

    #sweeper()
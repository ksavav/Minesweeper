import random

class GameBoard:
    def __init__(self):
        super().__init__()

    def creat_board(self, colums, rows):
        self.rows_on_board = []
        self.full_board = []

        for i in range(0, rows + 2):
            self.rows_on_board = []

            if i == 0 or i == rows + 1:
                self.rows_on_board = [-1] * (colums + 2)
            
            else:
                for j in range (0, colums + 2):
                    if j == 0 or j == colums + 1:
                        self.rows_on_board.append(-2)

                    else:
                        if random.randint(1, 100) <= 10: # <== chance of spawning a mine
                            self.rows_on_board.append(9) # the mines symbol

                        else:
                            self.rows_on_board.append(0) # this should show how many mines is around

            self.full_board.append(self.rows_on_board)

        return self.full_board

    def creat_numbers_of_mines(self, full_board):
        for i in range(1, len(self.full_board) - 1):
            for j in range(1, len(self.full_board[i]) - 1):
                k = 0
                if full_board[i][j] == 0:
                    if full_board[i][j + 1] == 9: k += 1
                    if full_board[i][j - 1] == 9: k += 1
                    if full_board[i + 1][j + 1] == 9: k += 1
                    if full_board[i - 1][j - 1] == 9: k += 1
                    if full_board[i + 1][j] == 9: k += 1
                    if full_board[i - 1][j] == 9: k += 1
                    if full_board[i + 1][j - 1] == 9: k += 1
                    if full_board[i - 1][j + 1] == 9: k += 1

                    full_board[i][j] = k


    def print_board(self, full_board):
        for i in range(len(self.full_board)):
            for j in range(len(self.full_board[i])):
                if self.full_board[i][j] == -1: print("-", end = "")
                
                elif self.full_board[i][j] == -2: print("|", end = "")
                
                elif self.full_board[i][j] == 9: print("*", end = "")

                elif self.full_board[i][j] == 0: print(" ", end = "") #heres a square ■

                else: print(self.full_board[i][j], end = "")
            
            print()

        #print(full_board)
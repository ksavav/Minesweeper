import random

class GameBoard:
    def __init__(self):
        super().__init__()


    def createBoard(self, colums, rows, bomb_chance):
        self.rows_on_board = []
        self.full_board = []

        for i in range(0, rows + 2):
            self.rows_on_board = []

            if i == 0 or i == rows + 1:
                self.rows_on_board = [-1] * (colums + 2) # vertical border
            
            else:
                for j in range (0, colums + 2):
                    if j == 0 or j == colums + 1:
                        self.rows_on_board.append(-2) # horizontal border

                    else:
                        if random.randint(1, 100) <= bomb_chance: # <== chance of spawning a mine
                            self.rows_on_board.append(9) # the mines symbol

                        else:
                            self.rows_on_board.append(0) # non bomb fields

            self.full_board.append(self.rows_on_board)

        return self.full_board


    def createNumbersOfMines(self, full_board):
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

    # for debuging without GUI
    # def printBoard(self, full_board, used_cords):
    #     z = 1
    #     for i in range(0, len(self.full_board)): 
    #         for j in range(len(self.full_board[i])):
    #             if i == 0 and j == 0: 
    #                 print("  ", end = '')
    #                 for k in range(0, len(self.full_board[i]) - 1): print("{: >3}".format(k), end = "")
    #                 print("\n")

    #             if i > 0 and i < len(self.full_board) - 1 and j == 0: 
    #                 print("{: >2}".format(z), end = "") 
    #                 z += 1

    #             if self.full_board[i][j] == -1: print(" _ ", end = "") #vertical border
                    
    #             elif self.full_board[i][j] == -2: print(" | ", end = "") #horizontal border

    #             elif [i, j] not in used_cords:
    #                 print(" ■ ", end = "")

    #             else:
    #                 if self.full_board[i][j] == 9: print(" * ", end = "") #bomb

    #                 elif self.full_board[i][j] == 0: print("   ", end = "") #blank field

    #                 else: print(f" {self.full_board[i][j]} ", end = "") #field near the bomb
            
    #         print("\n")

    #     #print(full_board)

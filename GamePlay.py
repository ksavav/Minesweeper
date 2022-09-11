from GameBoard import GameBoard

class GamePlay(GameBoard):
    used_cords = []

    def __init__(self):
        super().__init__()


    def playerMove(self, full_board, used_cord):
        # for console application 
        # while True:
        #     try:
        #         # user_move = input("Make your move. Type the number of the row and the number of the column u want to uncover (f.e. 9:2 <- row 9, column 2): \n")
                
        #         # user_move = user_move.split(":")
        #         # pos_x = int(user_move[0])
        #         # pos_y = int(user_move[1])

        #         # used_cord = [pos_x, pos_y]

        #         if used_cord not in self.used_cords:
        #             break
                
        #         else: print("You used thoes cords already!")
  
        #     except:
        #         if IndexError: print("Provide only two numbrs, first for the column and second for the row\n")
        #         elif ValueError: print("You should provide two numbers separated by ':'!\n")

        self.used_cords.append(used_cord)
        
        self.interactionWithBoard(full_board, used_cord)


    def interactionWithBoard(self, full_board, move):        
        if full_board[move[0]][move[1]] == 0:
            self.checkAllAround(full_board, move[0], move[1])


    def checkAllAround(self, full_board, row, column):
        for dx in range(-1 if (row > 0) else 0, 2 if (row < len(full_board)) else 1):
            for dy in range(-1 if (column > 0) else 0, 2 if (column < len(full_board[row])) else 1):
                #if (dx is not 0 and dy is not 0):
                if [row + dx, column + dy] not in self.used_cords: #and (full_board[row - 1][column + 1] != -1 or full_board[row - 1][column + 1] != -2):  
                    self.used_cords.append([row + dx, column + dy])

                    if full_board[row + dx][column + dy] == 0:
                        self.checkAllAround(full_board, row + dx, column + dy)

        #first value is a row, second is a cloumn 

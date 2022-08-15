import PySimpleGUI as sg
from GameBoard import GameBoard
from GamePlay import GamePlay
from Colors import Colors

class GameWindow:
    def __init__(self, rows, columns, bombs_chance):
        super().__init__()

        board = GameBoard()

        self.gp = GamePlay()
        
        self.full_board = board.createBoard(columns, rows, bombs_chance) #columns, rows

        board.createNumbersOfMines(self.full_board)

        self.createWindow(columns, rows)

        

    def createWindow(self, columns, rows):
        sg.change_look_and_feel('Black')
        COLUMNS = columns
        ROWS = rows   
        #table = [[True] * COLUMNS for _ in range(ROWS)]

        layout = [[sg.Text('MINESWEEPER', font='Default 25')],
                [sg.Text(size=(15,1), key='-MESSAGE-', font='Default 20')]]
        layout += [[sg.Button('Flag')]]
        layout += [[sg.Button(str('■'), size=(2, 2), pad=(0, 0), border_width = 0, key=(row,col), font=("Calibri", 15)) 
            for col in range(1, COLUMNS + 1)] for row in range(1, ROWS + 1)]

        layout += [[sg.Button('Exit')]]

        window = sg.Window("Minesweeper", layout)

        flag = False
        flaged_tiles = []

        while True:
            event, values = window.read()

            if event in (None, 'Exit'):
                break
            
            elif event == "Flag":
                flag = True

            elif flag == True:
                if [event[0], event[1]] not in self.gp.used_cords:
                    flaged_tiles.append([event[0], event[1]])
                    window[event].update("🚩", button_color = 'white')

                elif [event[0], event[1]] in flaged_tiles:
                    flaged_tiles.remove([event[0], event[1]])
                    window[event].update(self.full_board[event[0]][event[1]])
                    
                flag = False

            else:
                # user_move = event.split(":")
                pos_x = int(event[0])
                pos_y = int(event[1])

                user_move = [pos_x, pos_y]

                self.gp.playerMove(self.full_board, user_move)
                for x in range(1, ROWS + 1):
                    for y in range(1, COLUMNS + 1):
                        if ([x, y] in self.gp.used_cords) and ([x, y] not in flaged_tiles):
                            if self.full_board[x][y] == 0: 
                                window[(x, y)].update(" ")

                            elif self.full_board[x][y] == 9:
                                 window[(x, y)].update("💣")
                                 
                            else: window[(x, y)].update(self.full_board[x][y], button_color = Colors[self.full_board[x][y] - 1])
                            
        window.close()
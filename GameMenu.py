import PySimpleGUI as sg

class GameMenu:
     def createGameMenu(self):
        sg.theme('DarkTeal9')     

        layout = [
            [sg.Text('Please enter size of the board, and chance of spawnig the bomb:')],
            [sg.Text('Rows: ', size =(15, 1)), sg.InputText()],
            [sg.Text('Columns: ', size =(15, 1)), sg.InputText()],
            [sg.Text('Chance of spawning bombs: ', size =(15, 1)), sg.InputText()],
            [sg.Button("Submit"), sg.Button("Exit")]
        ]
        
        window = sg.Window('Start minesweeper', layout)

        while True:
                event, values = window.read()

                if event in (None, 'Exit'):
                    break
                
                elif event == "Submit":
                    window.close()
                    return int(values[0]), int(values[1]), int(values[2])

        window.close()   

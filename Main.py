#minesweeper

from GameWindow import GameWindow
from GameMenu import GameMenu

def sweeper():
    win = False
    lose = False

    menu = GameMenu()
    values = menu.createGameMenu()
    gw = GameWindow(values[0], values[1], values[2])


if __name__ == "__main__":
    sweeper()

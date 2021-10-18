import Globals
import random
import time
import msvcrt
import keyboard
from Classes import Menu
from Classes import HighscoreEntry

highscores = [
    HighscoreEntry("Marco", "if(True)"),
    HighscoreEntry("Balbo", "<3"),
    HighscoreEntry("Felix", 1337),
    HighscoreEntry("Marc", 420),
    HighscoreEntry("Benni", 69),
    HighscoreEntry("Dome", "UωU"),
]
tiles = []

def menuMain():
    match Menu("main", "main menu", Globals.dictMain).view():
        case "p":
            play()
        case "h":
            menuHighscores()
        case "s":
            menuSettings()
        case "c":
            exit()

def play():
    global tiles
    tiles = [0 for _ in range(Globals.width * Globals.height)]
    # set snake in center
    idxCenter = int(.5 * Globals.width) + int(.5 * Globals.height) * Globals.width
    tiles[idxCenter] = 2
    # place food
    for i in range(Globals.food):
        invalidFoodPos = True
        while invalidFoodPos:
            rand = random.randrange(Globals.width * Globals.height)
            if tiles[rand] == 0:
                invalidFoodPos = False
                tiles[rand] = 1
    while True:
        # input
        if keyboard.is_pressed("q"):
            print("input: {}".format("quit"))
        # update
        # updatePlayScreen()
        # sleep
        time.sleep(.1)

def updatePlayScreen():
    menu = Menu("play", "In-Game", {})
    #menu.printHeader()
    for i, val in enumerate(tiles):
        x = i % Globals.width
        y = int(i / Globals.width)
        if (x == 0): print("{}".format(Globals.prefixIndent), end="")
        cell = "{:>1}" if ord(Globals.tileValues[val]) > 9000 else "{:>2}"
        print(cell.format(Globals.tileValues[val]), end="")
        if x == Globals.width - 1: print("")

def menuHighscores():
    menu = Menu("highscores", "highscores", Globals.dictHighscores)
    menu.printHeader()
    menu.printOptions()
    print("{}|  {} | {}       Name | {}    Survived |".format(Globals.prefixIndent, Globals.dictIcons.get("placement"), Globals.dictIcons.get("name"), Globals.dictIcons.get("time")))
    print("{}|-----+---------------+----------------|".format(Globals.prefixIndent))
    for index, entry in enumerate(highscores):
        print("{}| {:>3} |{:>14} | {:>14} |".format(Globals.prefixIndent, index, entry.name, entry.score))
    print("\n")
    match menu.askInput():
        case "b":
            menuMain()

def menuSettings():
    match Menu("settings", "settings", Globals.dictSettings).view():
        case "b":
            menuMain()
        case "s":
            print("speed")

def main():
    #menuMain()
    play()

if __name__ == "__main__":
    main()
import random
import time
import msvcrt
import Globals
from classes.HighscoreEntry import HighscoreEntry
from classes.Menu import Menu
from classes.Snake import Snake

highscores = [
    HighscoreEntry("Marco", "if(True)"),
    HighscoreEntry("Balbo", "<3"),
    HighscoreEntry("Felix", 1337),
    HighscoreEntry("Marc", 420),
    HighscoreEntry("Benni", 69),
    HighscoreEntry("Dome", "UωU"),
]
tiles = []
food = []


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
    global tiles, food
    tiles = [0 for _ in range(Globals.width * Globals.height)]
    # set snake in center
    idxCenter = int(.5 * Globals.width) + \
        int(.5 * Globals.height) * Globals.width
    # place food
    food = []
    for i in range(Globals.food):
        invalidFoodPos = True
        while invalidFoodPos:
            rand = random.randrange(Globals.width * Globals.height)
            if not rand in food:
                invalidFoodPos = False
                food.append(rand)
    loop = True
    snake = Snake(idxCenter)
    print("snake created", snake.tiles)
    while loop:
        # input
        if (msvcrt.kbhit()):
            input = msvcrt.getwch()
            match input:
                case "w":
                    print('w up')
                    if (snake.up()):
                        print("collision")
                case "s":
                    print('s down')
                    # snake.down()
                case "a":
                    print('a left')
                    # snake.left()
                case "d":
                    print('d right')
                    # snake.right()
                case "q":
                    print('q close')
                    loop = False
                    menuMain()
                case _:
                    print("no binding", input)
            #print("input: {}, type: {}".format(input, type(input)))
        # update
        updatePlayScreen(snake.get(), food)
        # sleep
        time.sleep(.125)


def updatePlayScreen(snake, food):
    global tiles
    menu = Menu("play", "In-Game", {})
    print("snake", len(snake), len(food))
    # menu.printHeader()
    for i, val in enumerate(tiles):
        # coord
        x = i % Globals.width
        y = int(i / Globals.width)
        # add snake and food to tiles
        if i in food:
            tiles[i] = 1
        elif i in snake:
            tiles[i] = 2
        else:
            tiles[i] = 0
        # print
        if (x == 0):
            print("{}".format(Globals.prefixIndent), end="")
        cell = "{:>1}" if ord(Globals.tileValues[tiles[i]]) > 9000 else "{:>2}"
        print(cell.format(Globals.tileValues[tiles[i]]), end="")
        if x == Globals.width - 1:
            print("")


def menuHighscores():
    menu = Menu("highscores", "highscores", Globals.dictHighscores)
    menu.printHeader()
    menu.printOptions()
    print("{}|  {} | {}       Name | {}    Survived |".format(Globals.prefixIndent, Globals.dictIcons.get(
        "placement"), Globals.dictIcons.get("name"), Globals.dictIcons.get("time")))
    print("{}|-----+---------------+----------------|".format(Globals.prefixIndent))
    for index, entry in enumerate(highscores):
        print("{}| {:>3} |{:>14} | {:>14} |".format(
            Globals.prefixIndent, index, entry.name, entry.score))
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
    # menuMain()
    play()


if __name__ == "__main__":
    main()

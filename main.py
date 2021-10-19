import random
import time
import msvcrt
import Globals
from classes.HighscoreEntry import HighscoreEntry
from classes.Menu import Menu
from classes.Snake import Snake

highscores = []
tiles = []
food = []
snake = None
loopSleep = .25

def menuMain():
    match Menu("main", "main menu", Globals.dictMain).view():
        case "p":
            play()
        case "h":
            menuHighscores()
        case "s":
            menuSettings()
        case "q":
            exit()

def play(countdown = 3):
    global tiles, food, snake
    tiles = [0 for _ in range(Globals.width * Globals.height)]
    # set snake in center 1/3 left
    idxCenter = int(.33 * Globals.width) + \
        int(.5 * Globals.height) * Globals.width
    # place food
    loop = True
    snake = Snake(idxCenter)
    food = []
    dirs = ["w", "a", "s", "d"]
    # starting direction
    dir = dirs[3]
    # create initial food
    regenFood(snake.get())
    # countdown and show controls
    while countdown > 0:
        countdown -= 1
        updatePlayScreen(
            snake.get(),
            food,
            "time",
            "Starting in {} seconds".format(countdown)
        )
        time.sleep(1)
    # game loop
    while loop:
        moveIndex = -1
        if (msvcrt.kbhit()):
            input = msvcrt.getwch()
            # directional input
            if input in dirs:
                # 180 deg turn prevention
                if dirs.index(dir) % 2 == dirs.index(input) % 2:
                    print("0 or 180 DEG BLOCK")
                else: dir = input
            elif input == "q":
                loop = False
                menuMain()
        # move
        match dir:
            case "w": moveIndex = snake.up()
            case "a": moveIndex = snake.left()
            case "s": moveIndex = snake.down()
            case "d": moveIndex = snake.right()
        # react
        if (moveIndex == -1):
            #collision
            loop = False
            menuGameEnd()
        elif moveIndex in food:
            snake.eat()
            food.remove(moveIndex)
        # update
        snakeIdx = snake.get()
        regenFood(snakeIdx)
        updatePlayScreen(snakeIdx, food)
        # sleep
        time.sleep(loopSleep)

def regenFood(snake):
    global food
    for i in range(Globals.food - len(food)):
        invalidFoodPos = True
        while invalidFoodPos:
            rand = random.randrange(Globals.width * Globals.height)
            if not rand in food and not rand in snake:
                invalidFoodPos = False
                food.append(rand)

def updatePlayScreen(snake, food, icon = "play", message = "In-Game"):
    global tiles
    menu = Menu(icon, message, {})
    menu.printHeader()
    print("{}(wasd) {} Move | (q) {} Quit\n".format(
        Globals.prefixIndent,
        Globals.dictIcons.get("controls"),
        Globals.dictIcons.get("quit")
    ))
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
        # PRINT
        # line start indent
        if (x == 0):
            print("{}".format(Globals.prefixIndent), end="")
        # values
        if type(Globals.tileValues[tiles[i]]) == type([]):
            iconIdx = i % (len(Globals.tileValues[tiles[i]]))
            print("{:>1}".format(Globals.tileValues[tiles[i]][iconIdx]), end="")
        else:
            print("{:>2}".format(Globals.tileValues[tiles[i]]), end="")
        # break
        if x == Globals.width - 1:
            print("")

def menuGameEnd():
    menu = Menu("defeat", "Defeat", Globals.dictGameEnd)
    msg = ""
    # ask username
    invalidInput = True
    username = ""
    while invalidInput:
        menu.printHeader()
        # ask
        print("{}{} Your name: ".format(Globals.prefixIndent, Globals.dictIcons.get("name")))
        if len(msg): print(msg)
        print("{}{}".format(Globals.prefixIndent, Globals.prefixInput), end="")
        username = input()
        # validate
        invalidInput = len(username) < 3
        # show mismatch
        if (invalidInput) : msg = "{} Has to be at least 3 chars".format(Globals.prefixError)
    # save to highscores
    print("{} Saved Highscore".format(Globals.prefixSuccess))
    # menu navigation
    menu.printHeader()
    score = len(snake.get())
    print("{}{} Name: {} | {} Score: {} pt(s).\n".format(
        Globals.prefixIndent,
        Globals.dictIcons.get("name"),
        username,
        Globals.dictIcons.get("highscores"),
        score
    ))
    # save highscore
    highscores.append( HighscoreEntry(username, score))
    highscores.sort(key=lambda x: x.score, reverse=True)
    menu.printOptions()
    match menu.askInput():
        case "b":
            menuMain()
        case "p":
            play()
        case "h":
            menuHighscores()

def menuHighscores():
    menu = Menu("highscores", "highscores", Globals.dictHighscores)
    menu.printHeader()
    menu.printOptions()
    if (len(highscores) > 0):
        print("{}|  {} | {}       Name | {}       Score |".format(
            Globals.prefixIndent,
            Globals.dictIcons.get("placement"),
            Globals.dictIcons.get("name"),
            Globals.dictIcons.get("score")
        ))
        print("{}|-----+---------------+----------------|".format(Globals.prefixIndent))
        for index, entry in enumerate(highscores):
            print("{}| {:>3} |{:>14} | {:>14} |".format(
                Globals.prefixIndent, index, entry.name, entry.score))
        print("\n")
    else:
        print("{}{} No Highscores yet. Start playing!".format(
            Globals.prefixIndent,
            Globals.dictIcons.get("placement")
        ))
    match menu.askInput():
        case "b":
            menuMain()

def menuSettings():
    menu = Menu("settings", "settings", Globals.dictSettings)
    menu.printHeader()
    menu.printOptions()
    match menu.askInput():
        case "b":
            menuMain()
        case "s":
            adjustSpeed()

def adjustSpeed():
    msg = ""
    # ask value
    invalidInput = True
    value = ""
    while invalidInput:
        # ask
        print("{}{} Set Game Speed: ".format(Globals.prefixIndent, Globals.dictIcons.get("speed")))
        print("{}{}".format(Globals.prefixIndent, Globals.prefixInput), end="")
        value = input()
        # validate
        try:
            value = float(value)
            if (value > 10 or value < 0) : raise ValueError("too large")
            loopSleep = .1 * (10 - float(value))
            invalidInput = False
            menuSettings()
        except ValueError:
            print("{}{} Only numbers between 0 and 10".format(Globals.prefixIndent, Globals.prefixError))

def main():
    menuMain()
    #play()

if __name__ == "__main__":
    main()

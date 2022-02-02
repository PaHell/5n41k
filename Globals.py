import os

# const
width = 56
height = 22
food = 5

# app
arch = "\33[90m i use arch btw \33[0m"
appName = "\33[6m\33[92m3p1l3p5y.py\33[0m\33[0m\33[90m - The Unhealthy Snake\33[0m"
dictIcons = {
    "app": "🐍",
    "main": "💠",
    "play": "🎮",
    "highscores": "🏆",
    "settings": "🔧",
    "quit": "❌",
    "back": "👈",
    "speed": "💨",
    "cursor": "💲",
    "placement": "🏅",
    "name": "😝",
    "score": "🎯",
    "defeat": "💀",
    "controls": "🔢",
    "time": "⏳"
}
tileValues = [
    "ꞏ",
    ["🍰", "🍺", "🍕", "🍪", "🍧"],
    ["🐍"]
]
# prefix
prefixIndent = "  "
prefixInput = "{} ".format(dictIcons.get("cursor"))
prefixOutput = "{}   💬".format(prefixIndent)
prefixError = "{}   ⛔".format(prefixIndent)
prefixSuccess = "{}   👌".format(prefixIndent)

# menus
dictMain = {
    "p": ["play", "Play"],
    "h": ["highscores", "View Highscores"],
    "s": ["settings", "Settings"],
    "q": ["quit", "Quit"],
}
dictSettings = {
    "b": ["back", "Back"],
    "s": ["speed", "Speed"],
}
dictHighscores = {
    "b": ["back", "Back"],
}
dictPlay = {
    "wasd": ["controls", "Move"],
    "q": ["quit", "Quit"],
}
dictGameEnd = {
    "b": ["back", "Back"],
    "p": ["play", "Play Again"],
    "h": ["highscores", "View Highscores"],
}


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

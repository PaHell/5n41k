import os

# const
width = 48
height = 24
food = 4

# app
appName = "3n41k"
dictIcons = {
    "app": "🐍",
    "main": "💠",
    "play": "🎯",
    "highscores": "🏆",
    "settings": "🔧",
    "close": "💤",
    "back": "👈",
    "speed": "💨",
    "cursor": "💲",
    "placement": "🏅",
    "name": "😝",
    "time": "⏳"
}
tileValues = [
    "·",
    "🍎",
    "🐍"
]
# prefix
prefixIndent = "  "
prefixInput = "{0} {1} ".format(prefixIndent, dictIcons.get("cursor"))
prefixOutput = "{0}    -> ".format(prefixIndent)

# menus
dictMain = {
    "p": ["play", "Play a Game"],
    "h": ["highscores", "View Highscores"],
    "s": ["settings", "Settings"],
    "c": ["close", "Close Game"],
}
dictSettings = {
    "b": ["back", "Back"],
    "s": ["speed", "Speed"],
}
dictHighscores = {
    "b": ["back", "Back"],
}
dictPlay = {
    "q": ["quit", "quit"],
}

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
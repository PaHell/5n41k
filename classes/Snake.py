import Globals


class Snake:
    def __init__(self, index):
        print("Snake init", index)
        self.tiles = [index]

    def up(self):
        index = self.tiles[-1]
        if (index > Globals.width):
            self.tiles.append(index - Globals.width)
            self.tiles.pop()
            return False
        else:
            # collision
            return True

    def get(self):
        return self.tiles

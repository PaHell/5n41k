import Globals


class Snake:
    def __init__(self, index):
        self.tiles = [index]
        self.eaten = 0

    def eat(self):
        self.eaten += 1
    
    def move(self, index):
        # has eaten, dont pop() on next step
        if self.eaten > 0:
            self.eaten -= 1
        else:
            self.tiles.pop(0)
        # collision self
        if (index in self.tiles): index = -1
        # add move index
        self.tiles.append(index)
        return self.tiles[-1]

    def up(self):
        index = self.tiles[-1]
        if index > Globals.width - 1:
            return self.move(index - Globals.width)
        else: return self.move(
            Globals.width * (Globals.height - 1)
            + index % Globals.width
        )

    def down(self):
        index = self.tiles[-1]
        if index < Globals.width * (Globals.height - 1):
            return self.move(index + Globals.width)
        else: return self.move(index % Globals.width)

    def left(self):
        index = self.tiles[-1]
        if index % Globals.width > 0:
            return self.move(index - 1)
        else: return self.move(index + Globals.width - 1)
    
    def right(self):
        index = self.tiles[-1]
        if (index + 1) % Globals.width != 0:
            return self.move(index + 1)
        else: return self.move(index - Globals.width + 1)

    def get(self):
        return self.tiles

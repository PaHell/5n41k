import msvcrt
import Globals


class Menu:
    def __init__(self, icon, title, options):
        self.icon = icon
        self.title = title
        self.options = options

    def printHeader(self):
        Globals.clearTerminal()
        print("\n{}{} {}\n".format(Globals.prefixIndent,
              Globals.dictIcons.get("app"), Globals.appName))
        icon = Globals.dictIcons.get(
            self.icon) or Globals.dictIcons.get("default")
        print("{}{} {}\n".format(Globals.prefixIndent, icon, self.title.upper()))

    def printOptions(self):
        for key in self.options:
            [icon, name] = self.options.get(key)
            print("{}({}) {} {}".format(Globals.prefixIndent,
                  key, Globals.dictIcons.get(icon), name))
        print("\n")

    def askInput(self):
        inputFalse = True
        str = ""
        while (inputFalse):
            str = msvcrt.getwch()
            val = self.options.get(str)
            inputFalse = val == None
        #print("{}{} {}".format(Globals.prefixOutput, Globals.dictIcons.get(val[0]), val[1]))
        return str

    def view(self):
        self.printHeader()
        self.printOptions()
        return self.askInput()

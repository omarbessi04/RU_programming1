class Art:
    def __init__(self) -> None:
        self.SCREENSIZE = [100, 20]  # horizontal, vertical
        self.SPACES = self.SCREENSIZE[0] - 4
        self.LOGOSPACE = " " * (self.SCREENSIZE[0] - 78)

    def printLogo(self):
        logo = f"""|{self.LOGOSPACE}_____   __        _____   __   _______ _____         {self.LOGOSPACE} |
|{self.LOGOSPACE}___  | / /______ ____  | / /   ___    |___(_)________{self.LOGOSPACE} |
|{self.LOGOSPACE}__   |/ / _  __ `/__   |/ /    __  /| |__  / __  ___/{self.LOGOSPACE} |
|{self.LOGOSPACE}_  /|  /  / /_/ / _  /|  /     _  ___ |_  /  _  /    {self.LOGOSPACE} |
|{self.LOGOSPACE}/_/ |_/   \__,_/  /_/ |_/      /_/  |_|/_/   /_/     {self.LOGOSPACE} |"""
        print(logo)

    def printHLine(self):
        line = "-" * self.SCREENSIZE[0]
        print(line)

    def printVBorder(self, length=1):
        for i in range(length):
            print("|", " " * (self.SCREENSIZE[0] - 4), "|")

    def printMessageBorder(self, text=""):
        spacechange = len(text)
        if spacechange % 2 == 0:
            textspace = " " * ((self.SCREENSIZE[0] // 2) - spacechange // 2 - 1)
            print(f"|{textspace}{text}{textspace}|")
        else:
            textspace = " " * ((self.SCREENSIZE[0] // 2) - spacechange // 2 - 2)
            print(f"|{textspace}{text}{textspace} |")


class MainMenu(Art):
    def showMainMenu(self, border_message, button_options, user_choices):
        self.printHLine()
        self.printLogo()
        self.printHLine()
        self.printMessageBorder(f"{border_message}")
        self.printHLine()
        self.printVBorder(3)
        self.printMessageBorder("Choose option:")
        for user_choice in user_choices:
            self.printMessageBorder(user_choice)
        self.printVBorder(4)
        self.printHLine()
        self.printMessageBorder(f"Options: {', '.join(button_options)}")
        self.printHLine()

        input("Enter choice: ")


x = MainMenu()
bordermessage = "Welcome to NaN Air!"
options = ["1", "2", "3", "4"]
choices = ["1. Staff", "2. Voyages", "3. Planes", "4. Destination"]

x.showMainMenu(bordermessage, options, choices)

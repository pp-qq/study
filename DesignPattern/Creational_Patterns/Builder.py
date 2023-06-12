class Burger:
    def __init__(self):
        self.buns = None
        self.cheese = None
        self.patty = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self

    def build(self):
        return self.burger


burger = (
    BurgerBuilder()
    .addBuns("sesame")
    .addCheese("cheddar")
    .addPatty("beef")
    .build()
)
print(burger.buns)  # sesame
print(burger.cheese)  # cheddar
print(burger.patty)  # beef

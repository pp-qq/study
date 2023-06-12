class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)

    def createFishBurger(self):
        ingredients = ["bun", "cheese", "fish-patty"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)


burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()  # ['bun', 'cheese', 'beef-patty']
burgerFactory.createFishBurger().print()  # ['bun', 'cheese', 'fish-patty']
burgerFactory.createVeganBurger().print()  # ['bun', 'special-sauce', 'veggie-patty']

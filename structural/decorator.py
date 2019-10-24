from abc import ABC, abstractmethod


class CoffeeIngredient(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def describe(self):
        pass


class CoffeeCondimentDecorator(CoffeeIngredient):
    def __init__(self, coffee):
        self.coffee = coffee


class Milk(CoffeeCondimentDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 1.5

    def describe(self):
        return self.coffee.describe() + " + milk"


class Shot(CoffeeCondimentDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 1

    def describe(self):
        return self.coffee.describe() + " + shot"


class CoffeeBase(CoffeeIngredient):
    pass


class Liberica(CoffeeBase):
    def __init__(self):
        self.name = "Liberica coffee"
        self.cost = 5

    def get_cost(self):
        return self.cost

    def describe(self):
        return self.name


class Robusta(CoffeeBase):
    def __init__(self):
        self.name = "Robusta coffee"
        self.cost = 5

    def get_cost(self):
        return self.cost

    def describe(self):
        return self.name


def main():
    # base coffee
    coffee = Robusta()
    # add condiment
    coffee = Shot(Milk(Robusta()))

    print(f"{coffee.describe()} costs ${coffee.get_cost()}")


if __name__ == "__main__":
    main()

"""
- Provides an interface for creating objects in a superclass, but allows
  subclasses to alter the type of objects that will be created.
"""
from abc import ABC, abstractmethod


class Stall(ABC):
    @abstractmethod
    def prepare_food(self):
        pass


class HotdogStall(Stall):
    def prepare_food(self):
        print("Hotdog is ready.")
        return Hotdog()


class PizzaStall(Stall):
    def prepare_food(self):
        print("Pizza is ready.")
        return Pizza()


class Food(ABC):
    pass


class Hotdog(Food):
    pass


class Pizza(Food):
    pass


def main():
    pizza_stall = PizzaStall()
    hotdog_stall = HotdogStall()

    food = []
    for stall in [pizza_stall, hotdog_stall]:
        food.append(stall.prepare_food())


if __name__ == "__main__":
    main()

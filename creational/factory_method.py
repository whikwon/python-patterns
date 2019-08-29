from abc import ABC, abstractmethod


class Stall(ABC):
    @abstractmethod
    def create_product():
        pass


class HotdogStall(Stall):
    def prepare_food():
        return Hotdog()


class PizzaStall(Stall):
    def prepare_food():
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
        food.append(stall.prepare_food)


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod


class PizzaStore(ABC):
    @abstractmethod
    def prepare_peperroni():
        pass

    @abstractmethod
    def prepare_cheese():
        pass


class PizzaHut(PizzaStore):
    def prepare_peperroni():
        return BeefPepperoni()

    def prepare_cheese():
        return CheddarCheese()


class DominoPizza(PizzaStore):
    def prepare_peperroni():
        return PorkPepperoni()

    def prepare_cheese():
        return GoudaCheese()


class PizzaIngredient(ABC):
    pass


class Pepperoni(PizzaIngredient):
    pass


class BeefPepperoni(Pepperoni):
    pass


class PorkPepperoni(Pepperoni):
    pass


class Cheese(PizzaIngredient):
    pass


class CheddarCheese(Cheese):
    pass


class GoudaCheese(Cheese):
    pass


def main():
    pizzahut = PizzaHut()
    domino_pizza = DominoPizza()

    for store in [pizzahut, domino_pizza]:
        store.prepare_peperroni()
        store.prepare_cheese()


if __name__ == "__main__":
    main()

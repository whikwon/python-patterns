"""State Pattern"""

from abc import ABC, abstractmethod

menus = dict(cola=100, sprite=50, mirinda=40, fanta=50)


class BaseState(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def exchange(self):
        pass

    @abstractmethod
    def select_drink(self):
        pass

    @abstractmethod
    def insert_money(self, amount):
        pass


class WaitingState(BaseState):
    def exchange(self):
        self.machine.empty_money()

    def select_drink(self):
        print("Nothing happened.")

    def insert_money(self, amount):
        self.machine.cumulate_money(amount)
        if self.machine.amount >= min(menus.values()):
            self.machine.change_state(SelectDrinkState(self.machine))


class SelectDrinkState(BaseState):
    def exchange(self):
        self.machine.empty_money()
        self.machine.change_state(WaitingState(self.machine))

    def insert_money(self, amount):
        self.machine.cumulate_money(amount)
        if self.machine.amount < min(menus.values()):
            self.machine.change_state(WaitingState(self.machine))

    def select_drink(self, drink):
        self.machine.pullout_drink(drink)
        if self.machine.amount >= min(menus.values()):
            self.machine.change_state(WaitingState(self.machine))


class VendingMachine(object):
    def __init__(self):
        self.state = WaitingState(self)
        self.amount = 0

    def change_state(self, state):
        self.state = state

    def exchange(self):
        self.state.exchange()

    def insert_money(self, amount):
        self.state.insert_money(amount)

    def select_drink(self, drink):
        self.state.select_drink(drink)

    def empty_money(self):
        print(f"{self.amount} has returned. ([deposit]: 0)")
        self.amount = 0

    def cumulate_money(self, amount):
        self.amount += amount

    def pullout_drink(self, drink):
        price = menus[drink]
        if self.amount >= price:
            self.amount -= price
            print(f"Got {drink}. ([deposit]: {self.amount})")
        else:
            print(f"Not affordable. ([deposit]: {self.amount})")


def main():
    vending_machine = VendingMachine()

    vending_machine.insert_money(110)
    vending_machine.select_drink("cola")

    vending_machine.insert_money(30)
    vending_machine.select_drink("sprite")

    vending_machine.exchange()


if __name__ == "__main__":
    main()

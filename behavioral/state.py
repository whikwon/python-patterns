"""Vending Machine State Pattern

if amount of money < min(drink): waiting state
else: selecting drink state

TODO:
  - add current deposit for every transition.
  - rename variables.
"""
from abc import ABC


menus = dict(cola=100, sprite=50, mirinda=40, fanta=50)


class BaseState(ABC):

    def __init__(self):
        pass

    def exchange(self):
        pass

    def insert_money(self, amount):
        pass


class WaitingState(BaseState):

    def __init__(self, machine):
        self.machine = machine

    def exchange(self):
        print("Nothing happens")

    def select_drink(self):
        print("Nothing happens")

    def insert_money(self, amount):
        self.machine.cumulate_money(amount)
        if self.machine.amount >= min(menus.values()):
            self.machine.change_state(SelectDrinkState(self.machine))


class SelectDrinkState(BaseState):

    def __init__(self, machine):
        self.machine = machine

    def exchange(self):
        self.machine.change_state(WaitingState(self.machine))

    def insert_money(self, amount):
        self.machine.cumulate_money(amount)
        if self.machine.amount < min(menus.values()):
            self.machine.change_state(WaitingState(self.machine))

    def select_drink(self, drink):
        self.machine.click_item(drink)
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

    def cumulate_money(self, amount):
        self.amount += amount

    def insert_money(self, amount):
        self.state.insert_money(amount)

    def select_drink(self, drink):
        self.state.select_drink(drink)

    def click_item(self, drink):
        price = menus[drink]
        if self.amount >= price:
            self.amount -= price
            print(f"Got {drink}. [deposit]: {self.amount}")
        else:
            print(f"Not afforable. [deposit]: {self.amount}")


def main():
    vending_machine = VendingMachine()

    vending_machine.insert_money(50)
    vending_machine.insert_money(50)
    vending_machine.select_drink('cola')


if __name__ == "__main__":
    main()

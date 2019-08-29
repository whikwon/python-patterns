"""
Add item various functionalities in runtime.
"""

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteComponent(Component):
    def execute(self):
        print("A")


class BaseDecorator(Component):
    def __init__(self, wrappee):
        self.wrappee = wrappee

    def execute(self):
        self.wrappee.execute()


class ConcreteDecorator(BaseDecorator):
    def execute(self):
        super().execute()
        self.extra()

    def extra(self):
        print("B")


def main():
    component = ConcreteComponent()
    component = ConcreteDecorator(component)
    component.execute()


if __name__ == "__main__":
    main()

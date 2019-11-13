from abc import ABC, abstractmethod


class BaseCommand(ABC):
    def __init__(self, military_unit):
        self.military_unit = military_unit


class RetreatCommand(BaseCommand):
    def execute(self):
        self.military_unit.retreat()


class AttackCommand(BaseCommand):
    def execute(self):
        self.military_unit.attack()


class MilitaryComposite(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def describe(self):
        pass

    def simple_attack(self):
        print(f"{self.__class__.__name__} {self.name} attack!")

    def simple_retreat(self):
        print(f"{self.__class__.__name__} {self.name} retreat!")


class Soldier(MilitaryComposite):
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"{self.__class__.__name__}(name={self.name})")

    def attack(self):
        self.simple_attack()

    def retreat(self):
        self.simple_retreat()


class Commander(MilitaryComposite):
    def __init__(self, name):
        self.name = name

    def order(self, command):
        command.execute()

    def describe(self):
        print(f"{self.__class__.__name__}(name={self.name})")


class MilitaryUnit(MilitaryComposite):
    def __init__(self, name):
        self.name = name
        self.components = []

    def describe(self):
        print(f"{self.__class__.__name__}(name={self.name}, n={self.num_components})")
        for component in self.components:
            component.describe()

    def attack(self):
        self.simple_attack()
        for component in self.components:
            component.attack()

    def retreat(self):
        self.simple_retreat()
        for component in self.components:
            component.retreat()

    @property
    def num_components(self):
        return len(self.components)


class Company(MilitaryUnit):
    def __init__(self, name):
        super().__init__(name)

    def register(self, component):
        assert isinstance(component, Soldier)
        self.components.append(component)
        component.parent = self


class Battalion(MilitaryUnit):
    def __init__(self, name):
        super().__init__(name)
        self.components = []

    def register(self, component):
        assert isinstance(component, Company)
        self.components.append(component)
        component.parent = self


def main():
    print("======== Army description ========")
    alpha = Soldier("Alpha")
    beta = Soldier("Beta")
    omega = Company("Omega")

    omega.register(alpha)
    omega.register(beta)
    omega.describe()

    print("======== Order ========")
    attack_command = AttackCommand(omega)
    retreat_command = RetreatCommand(omega)
    commander = Commander("John")
    commander.order(attack_command)
    commander.order(retreat_command)


if __name__ == "__main__":
    main()

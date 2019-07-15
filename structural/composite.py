from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def print_information(self):
        pass


class DataEngineer(Employee):

    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name)


class DataEngineeringTeam(Employee):

    def __init__(self):
        self.team = []

    def add_component(self, component):
        self.team.append(component)

    def remove_component(self, component):
        self.team.remove(component)

    def print_information(self):
        for component in self.team:
            component.print_information()


def main():
    alex = DataEngineer("alex")
    john = DataEngineer("john")
    john.print_information()

    team = DataEngineeringTeam()
    team.add_component(alex)
    team.add_component(john)
    team.print_information()


if __name__ == "__main__":
    main()

from abc import ABC


class BaseCommand(ABC):

    def __init__(self, military_unit):
        self.military_unit = military_unit


class RetreatCommand(BaseCommand):

    def execute(self):
        self.military_unit.retreat()


class AttackCommand(BaseCommand):

    def execute(self):
        self.military_unit.attack()


class MilitaryUnit(ABC):

    def __init__(self, name, num_soldiers):
        self.name = name
        self.num_soldiers = num_soldiers


class Brigade(MilitaryUnit):
    """Number of men range from 1500 to 3500."""

    def __init__(self, name, num_soldiers):
        super().__init__(name, num_soldiers)
        assert 1500 <= self.num_soldiers < 3500

    def attack(self):
        print(f"{self.name}! Attack!!!")

    def retreat(self):
        print(f"{self.name}! Retreat!!!")


class CarrierPigeon(object):

    def __init__(self, name):
        self.name = name

    def convey(self, command):
        command.execute()


def main():
    brigade_A = Brigade("Alpha", 3000)
    attack_command = AttackCommand(brigade_A)
    retreat_command = RetreatCommand(brigade_A)

    mary = CarrierPigeon("Mary")

    mary.convey(attack_command)
    mary.convey(retreat_command)


if __name__ == "__main__":
    main()

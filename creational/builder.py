from abc import ABC, abstractmethod


class HouseBuilder(ABC):
    @abstractmethod
    def create_foundation(self):
        pass

    @abstractmethod
    def create_floor(self):
        pass

    @abstractmethod
    def create_room(self):
        pass

    @abstractmethod
    def create_door(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_roof(self):
        pass


class SingleFloorHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = "single floor house with\n"

    def create_foundation(self):
        self.house += " - foundation\n"

    def create_floor(self):
        self.house += " - floor\n"

    def create_room(self):
        self.house += " - room\n"

    def create_door(self):
        self.house += " - door\n"

    def create_window(self):
        self.house += " - window\n"

    def create_roof(self):
        self.house += " - roof\n"


class Director(object):
    def __init__(self, builder):
        self.builder = builder

    def create_single_floor_house(self):
        assert isinstance(self.builder, SingleFloorHouseBuilder)
        self.builder.create_foundation()
        self.builder.create_floor()
        self.builder.create_room()
        self.builder.create_door()
        self.builder.create_window()
        self.builder.create_roof()


def main():
    builder = SingleFloorHouseBuilder()
    director = Director(builder)

    director.create_single_floor_house()
    print(builder.house)


if __name__ == "__main__":
    main()

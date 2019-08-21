from abc import ABC


class Cook(object):
    def __init__(self, name):
        self.name = name

    def set_fan(self, fan):
        self.fan = fan

    def cook(self, menu):
        print(f"{self.name} prepared {menu} using {self.fan.name}")


class Pan(ABC):
    pass


class ChineseFryingPan(Pan):
    name = "ChineseFryingPan"


class SaucePan(Pan):
    name = "SaucePan"


def main():
    chinese_frying_pan = ChineseFryingPan()
    sauce_pan = SaucePan()

    cook = Cook("John")
    cook.set_fan(chinese_frying_pan)
    cook.cook("fried_rice")

    cook.set_fan(sauce_pan)
    cook.cook("soup")


if __name__ == "__main__":
    main()

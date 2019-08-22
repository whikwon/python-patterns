from abc import ABC


class Chef(object):
    def __init__(self, name):
        self.name = name

    def set_pan(self, pan):
        self.pan = pan

    def cook(self, menu):
        print(f"{self.name} prepared {menu} using {self.pan.name}")


class Pan(ABC):
    pass


class ChineseFryingPan(Pan):
    name = "ChineseFryingPan"


class SaucePan(Pan):
    name = "SaucePan"


def main():
    chinese_frying_pan = ChineseFryingPan()
    sauce_pan = SaucePan()

    chef = Chef("John")
    chef.set_pan(chinese_frying_pan)
    chef.cook("fried_rice")

    chef.set_pan(sauce_pan)
    chef.cook("soup")


if __name__ == "__main__":
    main()

"""
Provides convenient access to a particular part of the subsystem's functionality.
"""


class WeddingHall(object):
    def book(self):
        print("Booked a wedding hall.")


class FlowerShop(object):
    def buy(self):
        print("Bought some wedding flowers.")


class Singer(object):
    def book(self):
        print("Booked a singer to sing Wedding anthem.")


class WeddingPlanner(object):
    def prepare(self):
        hall = WeddingHall()
        flower_shop = FlowerShop()
        singer = Singer()

        hall.book()
        flower_shop.buy()
        singer.book()


def main():
    planner = WeddingPlanner()
    planner.prepare()


if __name__ == "__main__":
    main()

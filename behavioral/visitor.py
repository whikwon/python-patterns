from abc import ABC, abstractmethod


class Salesman(ABC):
    pass


class Door2DoorSalesman(Salesman):
    def visit_premium_customer(self):
        print("Hello sir, we have prepared a new product for you.")

    def visit_normal_customer(self):
        print("Hi, new product has been released. Would you take a look?")


class Customer(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PremiumCustomer(Customer):
    def accept(self, visitor):
        visitor.visit_premium_customer()


class NormalCustomer(Customer):
    def accept(self, visitor):
        visitor.visit_normal_customer()


def main():
    premium_customer = PremiumCustomer()
    normal_customer = NormalCustomer()

    salesman = Door2DoorSalesman()

    normal_customer.accept(salesman)
    premium_customer.accept(salesman)


if __name__ == "__main__":
    main()

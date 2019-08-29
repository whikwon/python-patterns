from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name):
        self.name = name
        self.schedule = []

    @abstractmethod
    def append_schedule(self):
        pass

    @abstractmethod
    def remove_schedule(self):
        pass


class Secretary(Worker):
    def __init__(self, name, ceo):
        super().__init__(name)
        self.ceo = ceo

    def append_schedule(self, schedule):
        self.ceo.append_schedule(schedule)
        print(f"Sir, {schedule} has been added.")

    def remove_schedule(self, schedule):
        self.ceo.remove_schedule(schedule)
        print(f"Sir, {schedule} has been cancelled.")


class CEO(Worker):
    def append_schedule(self, schedule):
        self.schedule.append(schedule)

    def remove_schedule(self, schedule):
        self.schedule.remove(schedule)


def main():
    ceo = CEO("Andy")
    secretary = Secretary("Amy", ceo)

    secretary.append_schedule("Meeting A")
    secretary.append_schedule("Meeting B")

    secretary.remove_schedule("Meeting A")


if __name__ == "__main__":
    main()

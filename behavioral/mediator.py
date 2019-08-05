class Dashboard(object):

    def __init__(self):
        self.racers = []

    def add_racer(self, racer):
        self.racers.append(racer)
        print(f"Racer {racer.name} has registered.")

    def update_status(self):
        for i, racer in enumerate(self.racers):
            print(f"[{i}]. Racer {racer.name} passed {racer.position}m")


class CarRacer(object):

    def __init__(self, name, dashboard):
        self._name = name
        self.dashboard = dashboard
        self._position = 0
        self._velocity = 0

    def slow_down(self):
        self._velocity -= 20
        if self._velocity < 0:
            self._velocity = 0

    def speed_up(self):
        self._velocity += 20

    def drive(self):
        self._position += self._velocity

    def update_status(self):
        self.dashboard.update_status()

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position


def main():
    dashboard = Dashboard()

    john = CarRacer("John", dashboard)
    mike = CarRacer("Mike", dashboard)
    anna = CarRacer("Anna", dashboard)

    dashboard.add_racer(john)
    dashboard.add_racer(mike)
    dashboard.add_racer(anna)

    john.speed_up()
    john.speed_up()
    mike.speed_up()
    anna.speed_up()

    john.drive()
    mike.drive()
    anna.drive()

    john.update_status()


if __name__ == "__main__":
    main()

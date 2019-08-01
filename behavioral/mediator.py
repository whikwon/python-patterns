from abc import ABC, abstractmethod


class SmartHomeSystem(ABC):

    @abstractmethod
    def _set_temperature(self):
        pass

    @abstractmethod
    def _set_tv_status(self):
        pass

    @abstractmethod
    def update_temperature(self):
        pass

    @abstractmethod
    def display(self):
        pass


class XiSmartHomeSystem(object):

    def __init__(self):
        self.tv_status = "off"
        self.temperature = 20

    def _set_temperature(self, temperature):
        self.temperature = temperature

    def update_temperature(self, *appliances):
        for app in appliances:
            app.set_temperature(self.temperature)

    def _set_tv_status(self, status):
        self.tv_status = status

    def display(self):
        print("===== XI SMART HOME SYSTEM =====")
        print(f"CURRENT TEMPERATURE: {self.temperature} degree")
        print(f"TV: {self.tv_status}")


class TemperatureController(object):

    def __init__(self, smart_home_system):
        self.smart_home_system = smart_home_system
        self.temperature = 20

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.smart_home_system._set_temperature(temperature)
        print(f"Set temperature to {temperature} by temperature controller.")


class TV(object):

    def __init__(self, smart_home_system):
        self.smart_home_system = smart_home_system
        self.temperature = 20
        self.status = "off"

    def set_temperature(self, temperature):
        self.temperature = temperature

    def turn_on(self):
        if self.status == "off":
            self.status = "on"
            self.smart_home_system._set_tv_status(self.status)
            print("Turned TV on")

    def turn_off(self):
        if self.status == "on":
            self.status = "off"
            self.smart_home_system._set_tv_status(self.status)
            print("Turned TV off")


def main():
    smart_home_system = XiSmartHomeSystem()
    temp_controller = TemperatureController(smart_home_system)
    tv = TV(smart_home_system)

    temp_controller.set_temperature(40)
    tv.turn_on()

    smart_home_system.update_temperature(tv)
    smart_home_system.display()


if __name__ == "__main__":
    main()

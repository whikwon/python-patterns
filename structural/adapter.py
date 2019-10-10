from abc import ABC, abstractmethod


class PowerPlug(ABC):
    @abstractmethod
    def plug_charger_in(item):
        pass


class EuropePowerPlug(PowerPlug):
    voltage = 220

    def plug_charger_in(self, item):
        assert self.voltage == item.voltage
        print(f"{item.__class__.__name__} has plugged into {self.__class__.__name__}")


class USPowerPlug(PowerPlug):
    voltage = 110

    def plug_charger_in(self, item):
        assert self.voltage == item.voltage
        print(f"{item.__class__.__name__} has plugged into {self.__class__.__name__}")


class IPhoneCharger(ABC):
    pass


class USIPhoneCharger(IPhoneCharger):
    voltage = 110


class EuropeIPhoneCharger(IPhoneCharger):
    voltage = 220


class PowerPlugAdapterFactory(ABC):
    @abstractmethod
    def get_powerplug(self):
        pass

    def set_voltage(self, item, voltage):
        assert hasattr(item, "voltage")
        item.voltage = voltage

    def plug_charger_in(self, item):
        self.set_voltage(item, self.adapter.voltage)
        self.adapter.plug_charger_in(item)


class USEuropePowerPlugAdapter(PowerPlugAdapterFactory):
    def __init__(self):
        self.adapter = self.get_powerplug()

    def get_powerplug(self):
        return EuropePowerPlug()


class EuropeUSPowerPlugAdapter(PowerPlugAdapterFactory):
    def __init__(self):
        self.adapter = self.get_powerplug()

    def get_powerplug(self):
        return USPowerPlug()


def main():
    us_iphone_charger = USIPhoneCharger()
    eur_iphone_charger = EuropeIPhoneCharger()

    eur_us_adapter = EuropeUSPowerPlugAdapter()
    eur_us_adapter.plug_charger_in(eur_iphone_charger)

    us_eur_adapter = USEuropePowerPlugAdapter()
    us_eur_adapter.plug_charger_in(us_iphone_charger)


if __name__ == "__main__":
    main()

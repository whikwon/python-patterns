from abc import ABC, abstractmethod


class PowerPlug(ABC):

    @abstractmethod
    def plug_charger_in(item):
        pass


class EuropePowerPlug(PowerPlug):
    voltage = 220

    def plug_charger_in(self, item):
        assert self.voltage == item.voltage
        print(f"{item.__class__.__name__} has plugged in")


class USPowerPlug(PowerPlug):
    voltage = 110

    def plug_charger_in(self, item):
        assert self.voltage == item.voltage
        print(f"{item.__class__.__name__} has plugged in")


class IPhoneCharger(ABC):
    pass


class USIPhoneCharger(IPhoneCharger):
    voltage = 110


class EuropeIPhoneCharger(IPhoneCharger):
    voltage = 220


class USEuropePowerPlugAdapter(EuropePowerPlug):
    voltage = 110


def main():
    eur_iphone_charger = USIPhoneCharger()
    power_plug = USEuropePowerPlugAdapter()
    power_plug.plug_charger_in(eur_iphone_charger)


if __name__ == "__main__":
    main()

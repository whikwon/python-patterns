"""
The flyweight suggests that you stop storing the extrinsic state inside the object.

- https://python-patterns.guide/gang-of-four/flyweight/
- https://howto.lintel.in/python-__new__-magic-method-explained/
- https://refactoring.guru/design-patterns/flyweight/python/example
"""


class Flyweight(object):
    _instances = {}

    def __new__(cls, data_type):
        obj = cls._instances.get(data_type.key)
        if obj is None:
            cls._instances[data_type.key] = super().__new__(cls)
            cls.data_type = data_type
        else:
            print("Flyweight already exists")
        return cls._instances[data_type.key]

    def register(self, owner, plate):
        print(f"{self.data_type} / {owner} / {plate} registration completed.")


class VehicleInfo(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __repr__(self):
        return f"{self.brand} / {self.model} / {self.color}"

    @property
    def key(self):
        return "_".join([self.brand, self.model, self.color])


def register_car_to_police_database(vehicle_info, owner, plate):
    flyweight = Flyweight(vehicle_info)
    flyweight.register(owner, plate)


def main():
    vehicle_infos = [VehicleInfo("BMW", "X6", "Red"),
                     VehicleInfo("BMW", "X6", "Red")]

    register_car_to_police_database(vehicle_infos[0], "John", "CL234IR")
    register_car_to_police_database(vehicle_infos[1], "Mike", "CL234IR")


if __name__ == "__main__":
    main()

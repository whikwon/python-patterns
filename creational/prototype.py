"""
- https://www.reddit.com/r/Python/comments/657v4u/prototype_pattern_in_python/
"""
from copy import deepcopy


class Prototype(object):

    def clone(self, **attrs):
        obj = deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


class Human(Prototype):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


def main():
    john = Human(name="John", weight=70)
    cloned_john = john.clone(weight=50)

    print(f"Original {john.name}'s weight: {john.weight}")
    print(f"Original {john.name}'s id: {id(john)}")
    print(f"Cloned {john.name}'s weight: {cloned_john.weight}")
    print(f"Cloned {john.name}'s id: {id(cloned_john)}")


if __name__ == "__main__":
    main()

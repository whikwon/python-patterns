"""
https://www.slideshare.net/DamianGordon1/python-the-iterator-pattern
"""


class Collection(object):

    def __init__(self):
        self.data = []

    def __iter__(self):
        return Iterator(self.data)

    def add_item(self, x):
        self.data.append(x)


class Iterator(object):

    def __init__(self, data):
        self.data = data
        self.index = 0
        self.num_data = len(self.data)

    def __next__(self):
        if self.index < self.num_data:
            self.index += 1
            return self.data[self.index - 1]
        else:
            raise StopIteration()


def main():
    collection = Collection()
    collection.add_item(1)
    collection.add_item(2)
    collection.add_item(3)

    for item in collection:
        print(item)


if __name__ == "__main__":
    main()

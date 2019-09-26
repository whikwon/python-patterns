class Auctioneer(object):
    def __init__(self, item, init_price):
        self.item = item
        self.bid = init_price
        self.highest_bidder = "No one"
        print(f"Bidding for '{item}' bidding starts at ${init_price}")

    def accept_bid(self, user, bid):
        if bid > self.bid:
            self.bid = bid
            self.highest_bidder = user
        else:
            print(f"{user}, your bid must be higher than the highest current bid.")

    def announce_price(self):
        print(f"Current highest bid: ${self.bid}, {self.highest_bidder}")


class Bidder(object):
    def __init__(self, name, auctioneer):
        self.name = name
        self.auctioneer = auctioneer

    def bid(self, price):
        self.auctioneer.accept_bid(self.name, price)
        self.auctioneer.announce_price()


def main():
    init_price = 100
    item = "Lionel Messi Signed Ball"
    auctioneer = Auctioneer(item, init_price)

    john = Bidder("John", auctioneer)
    mike = Bidder("Mike", auctioneer)
    anna = Bidder("Anna", auctioneer)

    john.bid(120)
    mike.bid(110)
    anna.bid(150)


if __name__ == "__main__":
    main()

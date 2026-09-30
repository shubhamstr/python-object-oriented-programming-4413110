# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable
from dataclasses import dataclass

@dataclass(eq=False)
class Asset():
    price: float

    def __eq__(self, value):
        return self.price == value.price

    def __gt__(self, value):
        return self.price > value.price

    def __lt__(self, value):
        return self.price < value.price

    def __ge__(self, value):
        return self.price >= value.price

    def __le__(self, value):
        return self.price <= value.price


@dataclass(eq=False)
class Stock(Asset):
    ticker: str
    company: str


@dataclass(eq=False)
class Bond(Asset):
    description: str
    duration: int
    interest: float

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)

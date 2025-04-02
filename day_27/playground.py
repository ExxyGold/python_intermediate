def add(*args):
    sum = 0
    for n in args:
        sum += n

    print(sum)


add(6,7,8,9,10)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add = 3, multiply = 5)



class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

car = Car(make = 21, model = "GT-R")

print(car.make)
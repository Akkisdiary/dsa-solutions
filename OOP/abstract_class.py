from abc import ABC, abstractmethod


class Car(ABC):
    # __metaclass__ = ABCMeta
    def __init__(self):
        print("Car created")

    @abstractmethod
    def mileage(self):
        pass

    def concrete(self):
        print("concrete")


class Hyundai(Car):
    def __init__(self):
        # super().__init__()
        print("Hyundai created")

    # def mileage(self):
    #     print("over budget")


class Maruti(Hyundai):
    def __init__(self):
        super().__init__()
        print("Maruti created")

    # def mileage(self):
    #     print("in budget")


# a = Car()

h = Hyundai()
print(h)

m = Maruti()
print(m)
# print(m.mileage())

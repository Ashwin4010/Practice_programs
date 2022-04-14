def add(*args):
    sum = 0
    for numbers in args:
        sum += numbers
    return sum

print(add(1,2,3,4,5,6))

def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3,multiply=5)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="nissan")
print(my_car.make)
print(my_car.model)
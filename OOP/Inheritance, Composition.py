#Inheritance and composition
class Engine():
    def start(self):
        pass
    def stop(self):
        pass
class ElectricEngine(Engine): # Is-A Engine
    pass
class V8Engine(Engine): # Is-A Engine
    pass
class Car():
    engine_cls = Engine
    def __init__(self):
        self.engine = self.engine_cls() # Has-A Engine
    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom!'
            .format(
                self.engine.__class__.__name__,
                self.__class__.__name__)
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()
class RaceCar(Car): # Is-A Car
    engine_cls = V8Engine

class CityCar(Car): # Is-A Car
    engine_cls = ElectricEngine
class F1Car(RaceCar): # Is-A RaceCar and also Is-A Car
    engine_cls = V8Engine

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]
for car in cars:
    car.start()

#Validity check - is instance check

car = Car()
racecar = RaceCar()
f1car = F1Car()
cars = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
car_classes = [Car, RaceCar, F1Car]
for car, car_name in cars:
    for class_ in car_classes:
        belongs = isinstance(car, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)

#inheritance check - for subclasses remember a class is a subclass of itself
for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1, class2)
        msg = '{0} a subclass of'.format(
            'is' if is_subclass else 'is not')
        print(class1.__name__, msg, class2.__name__)





#Accessing a base class  
#  EQUAL   class A: pass    or    class A(): pass   or    class A(object):pass


class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_

class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_

ebook = Ebook('Learn Python', 'UDEMY', 1310, 'PDF')
print(ebook.title) # Learning Python
print(ebook.publisher) # UDEMY
print(ebook.pages) # 360
print(ebook.format_) # PDF

#Multiple Inheritance
#class SportsCar(CityCar, f1Car):
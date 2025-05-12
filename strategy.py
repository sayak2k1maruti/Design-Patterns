from abc import ABC, abstractmethod
class FlyBehaviour:
    @abstractmethod
    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I'm flying with wing!!")

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")

class QuackBehaviour:
    @abstractmethod
    def quack(self):
        raise NotImplementedError

class Quack(QuackBehaviour):
    def quack(self):
        print("Quack, Quack!")

class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak!")

class CantQuack(QuackBehaviour):
    def quack(self):
        print("...")

class Duck:
    _fly_behaviour = None
    _quack_behaviour = None

    @property
    def fly_behaviour(self):
        return self._fly_behaviour
    
    @fly_behaviour.setter
    def fly_behaviour(self, fly_behaviour):
        self._fly_behaviour = fly_behaviour

    @property
    def quack_behaviour(self):
        return self._quack_behaviour
    
    @quack_behaviour.setter
    def quack_behaviour(self, quack_behaviour):
        self._quack_behaviour = quack_behaviour

    def perform_fly(self):
        self.fly_behaviour.fly()

    def perform_quack(self):
        self.quack_behaviour.quack()
    
    @abstractmethod
    def display(self):
        raise NotImplementedError
    
    @abstractmethod
    def swim(self):
        print("I can swim :-)")


class RealDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyWithWings()
        self.quack_behaviour = Quack()
    
    def display(self):
        print("I'm a real duck")

class ToyDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyNoWay()
        self.quack_behaviour = Squeak()
    
    def display(self):
        print("I'm a toy duck")

real_duck = RealDuck()
toy_duck = ToyDuck()

wood_duck = Duck()
wood_duck.fly_behaviour = FlyNoWay()
wood_duck.quack_behaviour = Quack()

for d in [real_duck, toy_duck]:
    d.display()
    d.perform_fly()
    d.perform_quack()
    d.swim()
    print("_"*10)

print("I am a wood duck")
wood_duck.perform_fly()
wood_duck.perform_quack()
wood_duck.swim()
from abc import ABC, abstractmethod
class Articles(ABC):
    def __init__(self, test):
        self.test = test
    @abstractmethod
    def expense(self):
        pass
    def __str__(self):
        return str(self.test)
class Overcoat(Articles):
    @property
    def expense(self):
        return self.test / 6.5 + 0.5
class ensemble(Articles):
    @property
    def expense(self):
        return self.test * 2 + 0.3
z = Overcoat(63)
d = ensemble(1.75)
print(z)
print(z.expense)
print(d.expense)




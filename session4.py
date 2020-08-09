from numbers import Real
import random
import math
import cmath
class Qualean():
    def __init__(self,x,ind=0):
            self.ind = ind 
            if self.ind == 0:
                self.real = x
            else:
                self._real = round(x,10)

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self,x):
        try:
            if isinstance(x, Real) and (x in {-1,0,1}):
                self._real = round(random.uniform(-1, 1) * x ,10)

            else:
                raise AttributeError('Invalid input')
        except:
            raise AttributeError('Invalid input') 
        finally:
            pass

    def  __and__(self, value):
            return self._real if not bool(self._real) else value._real


    def __or__(self,value):
        return self._real if bool(self._real) else value._real

    def __repr__(self):
        return f'Value of the Qualean object is : {self.real}'

    def __str__(self):
        return f'Qualean object value is : {self.real}'

    def __add__(self,other):
        return Qualean(other._real + self._real,1)

    def __eq__(self,other):
        return (self.__class__ == other.__class__) and (self._real == other._real)

    def __float__(self):
        return float(self._real)

    def __ge__(self,other):
        return (self.__class__ == other.__class__) and (self.real >= other.real)

    def __gt__(self,other):
        return (self.__class__ == other.__class__) and (self.real > other.real)

    def __le__(self,other):
        return (self.__class__ == other.__class__) and (self._real <= other._real)

    def __lt__(self,other):
        return (self.__class__ == other.__class__) and (self._real < other._real)

    def __mul__(self,other):
        return Qualean(other._real * self._real,1)

    def __bool__(self):
        return self.real != 0

    def __invertsign__(self):
        return (-1) * self.real

    def __sqrt__(self):
        if self.real >=0:
            return math.sqrt(self.real)
        else:
            return cmath.sqrt(self.real)

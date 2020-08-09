Help on class Qualean in module builtins:

class Qualean(object)
=========================
The Qualean class that is inspired by Boolean+Quantum concepts. 
We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. 
The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and 
multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 
It implements these functions (with exactly the same names)
__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__


#and 
-----
This class checks the and operator for two values . If the first value is false then it does not check the second one and returns false
        def  __and__(self, value):
            return self._real if not bool(self._real) else value._real
    
# or
------  
This class checks the or operator for two values . If the first value is Truee then it does not check the second one and returns True
       
    def __or__(self,value):
        return self._real if bool(self._real) else value._real
    
#repr
-------

This is the representation class. When you create an instance of the class and try to view it, this functions returns the value to you

    def __repr__(self):
        return f'Value of the Qualean object is : {self.real}'
#str
------
This function returns the string value of the object 
   
    def __str__(self):
        return f'Qualean object value is : {self.real}'
#add
-------
This function adds the objects and return the sum. It actually takes the real part of the number
 
    def __add__(self,other):
        return Qualean(other._real + self._real,1)
    
#eq
-------
This function checks if both the numbers are same or not
 
   
    def __eq__(self,other):
        return (self.__class__ == other.__class__) and (self._real == other._real)
    
    
#float
--------

provides the float value of the given object
    def __float__(self):
        return float(self._real)
#ge
-----
Gien two objects it returns if the numbers are either greater than or equal to each other 
    
    def __ge__(self,other):
        return (self.__class__ == other.__class__) and (self.real >= other.real)
#gt
------
Gien two objects it returns if the numbers are either greater than or not
 
    def __gt__(self,other):
        return (self.__class__ == other.__class__) and (self.real > other.real)
    
#le
-----
Gien two objects it returns if the numbers are either less than or equal to each other 
    def __le__(self,other):
        return (self.__class__ == other.__class__) and (self._real <= other._real)
 
 # lt
------
Gien two objects it returns if the numbers are either less than or not
    
    def __lt__(self,other):
        return (self.__class__ == other.__class__) and (self._real < other._real)
    
#mul
-----
GIven two objects of the class it multiplies and returns the result

    def __mul__(self,other):
        return Qualean(other._real * self._real,1)
 
#bool
-------
Provides the bool value. It returns true for everything except 0
 
    def __bool__(self):
        return self.real != 0
 
 # invertsign
 ----------------
 
 If just alters the sign of the real part of the object . for example if the given number is 1 then it returns -1 and vice versa
 
    def __invertsign__(self):
        return (-1) * self.real

# sqrt
--------

It returns the square root of the given imaginary number 

    def __sqrt__(self):
        if self.real >=0:
            return math.sqrt(self.real)
        else:
            return cmath.sqrt(self.real)
        
        
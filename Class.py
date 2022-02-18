

'print("Welcome to class of claseses")'

"""

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
    def miau(self):
        print("Miau hijuesupinchemadre")

class fall(Cat):
    def miau2(self):
        print("Wau wau que ha pasao?")

class dog(fall):
    def bark(self):
        print("miau wau soy un gatoperro")

fuk = dog("blanco",7)
print(fuk.legs)
"""
# fuk.miau()
# fuk.miau2()
# fuk.bark()

      #clases magic methods osea operradores como + y *
from enum import Flag
from queue import Queue
from re import S
from unittest import result


class Vector2D:
    def __init__(self,x,y):
        self.x =x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

f = Vector2D(5,7)
s = Vector2D(2,6)
result = f+s
print(result.x)
print(result.y)        

 #Hidden function

class queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    

    def push(self, value):
        self._hiddenlist.insert(0, value)
    
    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    

    @property
    def pineaple_allowed(self):
        return False

    @pineaple_allowed.setter
    def pineaple_allowed(self,value):
        if value:
            password = input("Enter passwor:")
            if password == "aixcaduy":
                self._pineaple_allowed = value
            else:
                raise ValueError("Intruso como que piza con piña")
        
    
pizza = Pizza(["QUESINO", "tomato"])
print(pizza.pineaple_allowed)
pizza.pineaple_allowed = True
print(pizza.pineaple_allowed)
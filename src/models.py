'''
CSC3020 - Software Engineering Fundamentals - Fall 2025
Instructor: Thyago Mota
Description: Simple models for OOP Practice
'''

import math 

class Rectangle: 

    DEFAULT_MEASURE = 1

    def __init__(self, width: int = DEFAULT_MEASURE, height: int = DEFAULT_MEASURE):
        self._width = max(width, Rectangle.DEFAULT_MEASURE)
        self._height = max(height, Rectangle.DEFAULT_MEASURE)

    @property 
    def width(self) -> int: 
        return self._width
    
    @width.setter 
    def width(self, width: int): 
        if width > 0: 
            self._width = width

    @property 
    def height(self) -> int: 
        return self.height
    
    @height.setter 
    def height(self, height: int): 
        if height > 0: 
            self._height = height

    def area(self) -> float: 
        return self._width * self._height
    
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)
    
    def diagonal(self) -> float:
        return math.sqrt(self.width**2 + self.height**2)
    
    def __str__(self) -> str: 
        return f'({self._width}, {self._height})'
    
# TODO use singleton to make sure only 1 instance of rectangle exists
class SingletonRectangle: 

    _instance = None

    @classmethod
    def get_instance(cls, width, height) -> Rectangle: 
        pass
    
class Vehicle: 

    def __init__(self, manufacturer: str, model: str, year: str): 
        self._manufacturer = manufacturer 
        self._model = model 
        self._year = year 

    def __str__(self) -> str: 
        return f'{self._manufacturer} {self._model} ({self._year})'
    
class Car(Vehicle):

    def __init__(self, manufacturer: str, model: str, year: str, type: str): 
        super().__init__(manufacturer, model, year)
        self._type = type

    def __str__(self) -> str: 
        return f"{super().__str__()} - {self._type}"
    
class Truck(Vehicle):

    DEFAULT_CLASSIFICATION = 1

    def __init__(self, manufacturer: str, model: str, year: str, classification: int): 
        super().__init__(manufacturer, model, year)
        self._classification = max(classification, Truck.DEFAULT_CLASSIFICATION)

    def __str__(self) -> str: 
        return f"{super().__str__()} - {self._classification}"
    
class BSTNode: 

    def __init__(self): 
        self._value = None
        self._left  = None
        self._right = None   

    def add(self, value): 
        if not self._value: 
            self._value = value   
        elif value < self._value: 
            self._left = BSTNode._add(self._left, value)
        elif value > self._value: 
             self._right = BSTNode._add(self._right, value)

    @staticmethod
    def _add(current, value):
        if not current: 
            bst_node = BSTNode()
            bst_node._value = value 
            return bst_node
        if value < current._value: 
            current._left = BSTNode._add(current._left, value)
        elif value > current._value: 
             current._right = BSTNode._add(current._right, value)
        return current

    @staticmethod
    def _print(current, tabs = ""): 
        out = ""
        if current:
            out += tabs + str(current._value) + '\n'
            out += BSTNode._print(current._left, tabs + '   ')
            out += BSTNode._print(current._right, tabs + '   ')            
        return out
        
    def __str__(self):
        return BSTNode._print(self, '')
    
    @staticmethod
    def _in_order(current) -> list: 
        values = []
        if (current):
            values += BSTNode._in_order(current._left)
            values.append(current._value)
            values += BSTNode._in_order(current._right)
        return values
    
    # TODO: implement an iterator
    def __iter__(self):
        pass
    
    def __next__(self):
        pass

    # TODO: replace the iterator with a generator
    # def __iter__(self): 
    #     pass
    
    # def _in_order_gen(self, node):
    #     pass

class MyNumbers:

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

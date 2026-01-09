from abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self,shape_type):
        self.shape_type=shape_type
        
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radiius):
        super().__init__("Circle")
        self.radius=radiius
        
    def calculate_area(self):
        return pi * self.radius**2
    
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width=width
        self.height=height
        
    def calculate_area(self):
        return self.width * self.height
    
    
if __name__=="__main__": 
    C=Circle(5)
    print(C.calculate_area())

    R=Rectangle(5,4)
    R.calculate_area()
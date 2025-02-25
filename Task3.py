class Shape:
    def __init__(self):
        pass 

    def area(self):
        return 0

    def parameters(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length 
    
    def parameters(self):
        return 4 * self.length 

shape = Shape()
print(shape.area())
print(shape.parameters())

square1 = Square(5)
print(square1.area())
print(square1.parameters())

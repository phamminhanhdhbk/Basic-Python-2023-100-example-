class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)   # Output: 4 6

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)   # Output: 4 6

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 * p2
print(p3.x, p3.y)   # Output: 8 15

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

p1 = Point(6, 8)
p2 = Point(2, 4)
p3 = p1 / p2
print(p3.x, p3.y)   # Output: 3.0 2.0

class Person:
    def __init__(self, name):
        self.name = name
        

import math

class Shape:
    """Base class for all shapes"""
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return 4 * self.side_length


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        # Using Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# Example usage:
shapes = [
    Circle(radius=5),
    Square(side_length=4),
    Triangle(side_a=3, side_b=4, side_c=5)
]

for shape in shapes:
    print(f"{type(shape).__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
'''Algorithm: Shape Class with Subclasses
Step 1: Define the Base Class (Shape)
Create a class Shape.
Define two methods:
area() (abstract method): raises a NotImplementedError.
perimeter() (abstract method): raises a NotImplementedError.
Step 2: Define the Circle Subclass
Create a subclass Circle that inherits from Shape.
Add an initializer (__init__) to accept the radius.
Implement the area method using the formula:
Area
=
π
×
radius
2
Area=π×radius 
2
 
Implement the perimeter method using the formula:
Perimeter
=
2
×
π
×
radius
Perimeter=2×π×radius
Step 3: Define the Square Subclass
Create a subclass Square that inherits from Shape.
Add an initializer (__init__) to accept the side_length.
Implement the area method using the formula:
Area
=
side_length
2
Area=side_length 
2
 
Implement the perimeter method using the formula:
Perimeter
=
4
×
side_length
Perimeter=4×side_length
Step 4: Define the Triangle Subclass
Create a subclass Triangle that inherits from Shape.
Add an initializer (__init__) to accept three sides: side_a, side_b, and side_c.
Implement the area method using Heron's formula:
Calculate the semi-perimeter:
s
=
side_a
+
side_b
+
side_c
2
s= 
2
side_a+side_b+side_c
​
 
Compute the area:
Area
=
s
×
(
s
−
side_a
)
×
(
s
−
side_b
)
×
(
s
−
side_c
)
Area= 
s×(s−side_a)×(s−side_b)×(s−side_c)
​
 
Implement the perimeter method as:
Perimeter
=
side_a
+
side_b
+
side_c
Perimeter=side_a+side_b+side_c
Step 5: Create and Test Objects
Create a list of shape objects:
A Circle with a given radius.
A Square with a given side length.
A Triangle with three given sides.
For each shape object:
Call the area method to compute the area.
Call the perimeter method to compute the perimeter.
Print the results in a formatted manner.'''
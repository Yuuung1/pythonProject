class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __copy__(self):
    #     return self.x, self.y

    def distance(self, other):
        dist = ((self.x - other.x) ** 2 + (self.x - other.y) ** 2) ** 0.5

class Triangle:
    pass

class Circle:
    pass

point = Point(1, 2)
print(point)
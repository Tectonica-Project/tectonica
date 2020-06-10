import math
from typing import Tuple, Union

class Vector:
    # Empty declaration for type annotations
    pass


class Vector:

    x: float
    y: float

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @staticmethod
    def xy_from_angle(angle, length) -> Tuple[float, float]:
        return math.cos(angle) * length, math.sin(angle) * length

    @classmethod
    def from_angle(cls, angle, length) -> Vector:
        return cls(*cls.xy_from_angle(angle, length))

    def _angle_get(self) -> float:
        return math.atan2(self.y, self.x)

    def _angle_set(self, angle):
        self.x, self.y = type(self).xy_from_angle(angle, self.length)
        return self # For chaining
    
    
    def _length_get(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def _length_set(self, length):
        self.x, self.y = type(self).xy_from_angle(self.angle, length)
        return self # For chaining

    @property
    def normal(self):
        return self.copy()._length_set(1)

    angle = property(_angle_get, _angle_set)
    length = property(_length_get, _length_set)

    def __neg__(self) -> Vector:
        return type(self)(-self.x, -self.y)

    def __add__(self, other: Vector) -> Vector:
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return type(self)(self.x - other.x, self.y - other.y)

    def dot(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: Vector) -> float:
        return self.length * other.length * math.sin(self.angle - other.angle)

    def project(self, other: Vector) -> Vector:
        return (self.length * math.cos(self.angle - other.angle)) * other.normal

    def rotated(self, delta_angle):
        new = self.copy()
        new.angle += delta_angle
        return new

    def copy(self) -> Vector:
        return type(self)(self.x, self.y)

    def __mul__(self, other: Union[float, int, Vector]) -> Union[float, int, Vector]:
        if isinstance(other, int) or isinstance(other, float):
            new = self.copy()
            new.x *= other
            new.y *= other
            return new

        elif isinstance(other, Vector):
            raise TypeError(f'Can\'t multiply vector by vector. Use .dot() or .cross() instead')

        else:
            raise TypeError(f'Can\'t multiply vector by {type(other)}')

    __rmul__ = __mul__

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    __str__ = __repr__

    def __list__(self):
        return [self.x, self.y]

    def __tuple__(self):
        return (self.x, self.y)

    def __getitem__(self, idx):
        return (self.x, self.y)[idx]
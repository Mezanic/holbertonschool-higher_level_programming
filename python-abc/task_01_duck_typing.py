#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Create abstract class Shape"""

    @abstractmethod
    def area(self):
        """Create abstract methode area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Create abstract method perimeter"""
        pass


class Circle(Shape):
    """Create class Circle"""

    def __init__(self, radius):
        """Constructor for Circle class"""

        self.__radius = abs(radius)

    def area(self):
        """Create methode for calculate area"""
        return pi * self.__radius**2

    def perimeter(self):
        """Create method for calculate perimeter"""
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """Create class Rectangle"""

    def __init__(self, width, height):
        """Constructor for Rectangle class"""

        self.__width = width
        self.__height = height

    def area(self):
        """Create methode for calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Create method for calculate perimeter"""
        return (self.__width + self.__height) * 2


def shape_info(shape):
    """
    Print area and perimeter of a shape

    Args:
        shape: object with area and perimeter
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

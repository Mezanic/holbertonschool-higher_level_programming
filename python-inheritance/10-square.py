#!/usr/bin/python3
"""This Module create an BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function for validate value

        Args:
            name: string to check
            value: integer to check
        Raises:
            TypeError: name must be an integer
            ValueError: name must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle inherit from BaseGeometry"""

    def __init__(self, width, height):
        """
        Init Rectangle Object

        Args:
            width: of the rectangle
            height: of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Return a string with theight andf the width of the rectangle"""
        return "[Rectangle] {}/{}" .format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square inherit from Rectangle"""

    def __init__(self, size):
        """
        Constructor for  Square

        Args:
            size: size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Print a string for square with rectangle in it """
        return "[Rectangle] {}/{}" .format(self.__size, self.__size)

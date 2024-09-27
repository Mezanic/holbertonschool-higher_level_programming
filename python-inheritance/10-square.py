#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle """

    def __init__(self, size):
        """Initializes a Rectangle object
        
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a square object"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of a square object named rectangle"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

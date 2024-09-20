#!/usr/bin/python3
"""This Module define a class for a Rectangle"""


class Rectangle:
    """ Define Class Rectangle

    Attributs:
    width (int): width of Recatngle
    height (int): Height of Rectangle

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize width and height of Rectangle

        Args:
        width (int): width of Recatngle
        height (int): Height of Rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of a Rectangle

        Return:
        width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Define the width of the rectangle

        Args:
            value (int): value for the width rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle

        Return:
            Height of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Define the height of the Rectangle

        Args:
            value(int): height of the rectangle

        Raises:
            Typerror: height must be an integer
            ValueError: height must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the aera of a Rectangle

        Return:
            Area of a Rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of a Rectangle

        Return:
            perimeter of a Rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0

        return 2 * (self.height + self.width)

    def __str__(self):
        """String representation of the Rectangle with '#' character"""

        symbol = str(self.print_symbol)
        return '\n'.join(symbol * self.__width for i in range(self.__height))

    def __repr__(self):
        """ String for represente the Rectangle height and width"""
        return "Rectangle ({}, {})".format(self.height, self.width)

    def __del__(self):
        """Delete instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Compare Rectangle and return the biggest rectangle based on area

        Args:
            rect_1: Frist Rectangle
            rect_2: Second Rectangle

        Return:
            Rectangle with biggest area

        Raises:
            TypeError: rect_1 or rect 2 must be an instance of Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2

        else:
            return rect_1

    def square(cls, size=0):
        """Return a new rectangle where width == height == size"""
        return cls(size, size)
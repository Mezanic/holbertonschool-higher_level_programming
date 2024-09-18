#!/usr/bin/python3

"""Module define a  class Square"""


class Square:
    """
    Class define Square with private instance attribut

    Attribut :
    size (int) : size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a  size of the square.

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Define the size of square

        Return
            size of the square as int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define the size of square with validation check

        Args:
            value(int): Value for the size of the square


        Raise:
            TypeError size must be an integer
            ValueError size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Function calculate the area of a square

        Return:

        Area of a Square
        """

        return self.__size ** 2

#!/usr/bin/python3

"""Module define a  class Square"""


class square:
    """
    Class define Square with private instance attribut

    Attribut :

    size (int) : size of the square
    area (int) : area of a square

    """


def __init__(self, size=0):
    """
    Initializes a  size of the square.

    Args:
    size (int): size of the square
    """
    self.__size = size

    @property
    def size(self):
        """
        Define the size of square

        Return
        size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define the size of square with validation check


        Raises:
            TypeError size must be an integer
            ValueError size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Function calculate the area of a square

        Return:

        Area of a Square
        """
        square_aera = size * size

        return square_aera

    def my_print(self):
        """ Print square with # character """

        if self.__size == 0:
            print("")

        else:
            for i in range(self.__size):
                print("#" * self.__size)

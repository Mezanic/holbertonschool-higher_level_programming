#!/usr/bin/python3

"""Module define a  class Square"""


class Square:
    """
    Class define Square with private instance attribut

    Attribut :

    size (int) : size of the square
    area (int) : area of a square

    """


def __init__(self, size=0, position=(0, 0)):
    """
    Initializes a  size of the square.

    Args:
    size (int): size of the square
    position (int): Position of square
    """
    self.__size = size
    self.__position = position

    @property
    def size(self):
        """ Return size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of square with validation check


        Raise:
            TypeError size must be an integer
            ValueError size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ Return the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of square

        Attribut:
        value (int): Tuple with the position

        Raises:

        TypeError: position must be a tuple of 2 positive integers
        ValueError: position must be a tuple of 2 positive integers
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for num in value:

            if not isinstance(num, int):
                raise TypeError
            ("position must be a tuple of 2 positive integers")

            if num < 0:
                raise TypeError
            ("position must be a tuple of 2 positive integers")

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

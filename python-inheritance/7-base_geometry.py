#!/usr/bin/python3
"""This Module create an BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Calculate area (WIP)"""
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

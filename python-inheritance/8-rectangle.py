#!/usr/bin/python3
"""This Module create an BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherit from BaseGeometry"""

    def __init__(self, width, height):
        """
        Init Rectangle Object

        Args:
            width: of the rectangle
            height: of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

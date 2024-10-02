#!/usr/bin/python3
"""Module with student class"""


class Student:
    """Defines student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes student instance.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that retrieves a dictionary representation of a Student.

        Args:
            attrs: List of string.
        """

        if attrs is None:
            return self.__dict__

        else:
            new_dict = {}

            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]

            return new_dict

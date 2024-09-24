#!/usr/bin/python3
""" This module define class MyList """


class MyList(list):
    """Subclass of list built in """

    def __init__(self):
        """Init MyList"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))

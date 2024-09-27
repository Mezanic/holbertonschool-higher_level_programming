#!/usr/bin/env python3
"""
This module extend the built in iterator by keeping track of
the number of item that have been iterate
"""


class CountedIterator:
    """
    Create class CountedIterator for count how many item have been iterate
    """

    def __init__(self, iterator_obj):
        """
        Constructor for CountedIterator

        Attribut:
            iterator_obj: object will be iterable
        """

        self.iterator_obj = iter(iterator_obj)
        self.count = 0

    def __iter__(self):
        """Start iteration"""
        return self

    def __next__(self):
        """Goes to the next item inside the iterarable and increment count"""
        try:
            next_item = next(self.iterator_obj)
            self.count += 1
            return next_item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        """ return the current value of the counter"""
        return self.count

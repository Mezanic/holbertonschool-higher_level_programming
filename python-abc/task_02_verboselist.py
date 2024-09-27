#!/usr/bin/env python3
"""
This module create a class Verboselist for print
a notification every time an item is added pr removed
"""


class VerboseList(list):
    """
    Create class Verboselist sub of list,
    for print notification when item are add or removed
    """

    def append(self, item):
        """Append item to the list and notification for it"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extend list with x number of item, print notification for it"""
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """Remove item from list and print notification for it"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove item at specified position of a list
        and print notificaiton for it
        """

        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

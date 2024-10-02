#!/usr/bin/python3
"""Module containing the pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal triangle.

    Args:
        n: The number of rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

#!/usr/bin/python3
"""
0-pascal_triangle: Contains pascal_triangle(n) method
                   that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        A list of lists of integers representing the Pascal's trangle of n.
        Returns and empty list if n <= 0.
    """
    # If n <= 0, return an empty list
    if n <= 0:
        return []

    # Initialize the triangle
    triangle = []

    for i in range(n):
        # Create a new row filled with 1s
        row = [1] * (i + 1)

        # Fill in the middle elements for the row
        if i > 1:  # This is first two rows, not middle elements
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the row to the triangle

    return triangle

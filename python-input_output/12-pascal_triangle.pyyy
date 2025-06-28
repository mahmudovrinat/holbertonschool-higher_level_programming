#!/usr/bin/python3
"""
Module that contains a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of size n.

    Args:
        n (int): Number of rows.

    Returns:
        list: Pascal’s triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # İlk sətrin başlanğıcı

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # Hər sətrin ilk elementi 1-dir

        # İç elementləri hesabla
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Hər sətrin son elementi 1-dir
        triangle.append(row)

    return triangle

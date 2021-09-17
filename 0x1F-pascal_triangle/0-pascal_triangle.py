#!/usr/bin/python3
'''
Returns list representing the Pascal's triangle of n:
'''


def pascal_triangle(n):
    '''returns empty list if n <= 0
       You can assume n will be always an integer'''
    pascal_integers = []
    if n <= 0:
        return pascal_integers
    for i in range(n):
        row = [1]
        if pascal_integers:
            last_row = pascal_integers[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_integers.append(row)
    return (pascal_integers)

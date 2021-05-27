#!/usr/bin/python3
"""0.Rain
"""


def rain(walls):
    """Prototype: def rain(walls)
       walls is a list of non-negative integers.
       Return: Integer indicating total amount of rainwater retained.
       Assume that the ends of the list (before index 0 and after
       index walls[-1]) are not walls, meaning they will not retain water.
       If the list is empty return 0.
    """
    i = maxleft = maxright = water = 0
    j = len(walls) - 1

    while i < j:
        if walls[i] < walls[j]:
            if walls[i] < maxleft:
                water += maxleft - walls[i]
            maxleft = max(maxleft, walls[i])
            i += 1
        else:
            if walls[j] < maxright:
                water += maxright - walls[j]
            maxright = max(maxright, walls[j])
            j -= 1

    return water

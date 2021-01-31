#!/usr/bin/python3
"""Open Lockboxes"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    keys = [0]
    for key in keys:
        box = boxes[key]
        for newkey in box:
            if newkey not in keys:
                if newkey < len(boxes):
                    keys.append(newkey)
    if len(keys) == len(boxes):
        return True
    else:
        return False
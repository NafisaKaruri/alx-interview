#!/usr/bin/python3
"""
canUnlockAll method to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of list of int): A list where each element represents
                                 a box containing keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked; otherwise, False.
    """
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List of unlocked boxes all closed except boxes[0]
    unlocked[0] = True
    keys = {0}  # Keys we got. Starting with the key to the first box
    unlocked_count = 1  # One unlocked box (boxes[0])

    while keys:
        # Get a key from the set then remove if
        current_box = keys.pop()
        # Loop over the found keys in the current box
        for key in boxes[current_box]:
            # Is the key for a valid box and the box is locked
            if key < n and not unlocked[key]:
                # Unlock the box
                unlocked[key] = True
                keys.add(key)
                unlocked_count += 1
                if unlocked_count == n:
                    return True

    # Check if all boxes have been unlocked
    return unlocked_count == n

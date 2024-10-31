#!/usr/bin/python3
"""
Contains the validUTF8 method.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): The data set to be tested.

    Return:
        - True if data is a valid UTF-8 encoding.
        - False if not a valid UTF-8 encoding.
    """
    # number of bytes expected in the UTF-8 character
    num_bytes = 0

    for byte in data:
        # Get the last 8 bits of the integer (the byte)
        byte &= 0xFF

        if num_bytes == 0:
            # Determine how many bytes the character consists of
            if (byte >> 7) == 0b0:  # 1-byte character
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False
        else:
            # We are expecting continuation bytes
            # A continuation byte should start with '10'
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # All bytes are processed, no pending bytes expected
    return num_bytes == 0

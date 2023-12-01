"""
Module: sequences
This module contains functions related to sequences (lists/tuples).
"""


def remove_duplicates(input_sequence):
    """
    Remove duplicates from a given sequence while maintaining the original order.

    Parameters:
    - input_sequence (list or tuple): Input sequence.

    Returns:
    list: A new sequence with duplicates removed.
    """
    seen = set()
    result = []

    for element in input_sequence:
        if element not in seen:
            seen.add(element)
            result.append(element)

    return result


# Testing remove_duplicates function
INPUT_SEQUENCE = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(INPUT_SEQUENCE)
print(result)

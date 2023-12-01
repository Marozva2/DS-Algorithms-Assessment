"""
Module: dictionaries
This module contains functions related to dictionaries.
"""
import string


def word_frequency(input_sentence):
    """
    Count the frequency of each word in the given sentence.

    Parameters:
    - input_sentence (str): Input sentence.

    Returns:
    dict: A dictionary containing word frequencies.
    """
    word_count = {}
    input_sentence = input_sentence.translate(
        str.maketrans("", "", string.punctuation))

    for word in input_sentence.lower().split():
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


# Testing word_frequency function
INPUT_SENTENCE = "This is a test sentence. This sentence is a test."
result = word_frequency(INPUT_SENTENCE)
print(result)

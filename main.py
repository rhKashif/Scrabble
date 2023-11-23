"""
Scrabble Game Main Module

This module is the entry point for a Scrabble-like word game implemented in Python. 

The game logic includes word validation and score calculation

Usage:
    Run this module to start the game. Players can interact with the game through 
    a command-line interface.

Note:
    This game is designed for educational purposes and as a demonstration of Python programming skills. 
    It is not intended for commercial use.

Author: Hassan Kashif
"""

def get_letter_score(letter: str) -> int:
    """
    Return the Score associated with a Given Letter in Scrabble.

    This function takes a single letter as input and returns its score based on Scrabble's scoring rules. 

    Parameters:
    word (str): The letter for which the score is to be returned. The letter should be a valid string 
                consisting of a uppercase or lowercase alphabetic character.

    Returns:
    int: The score of the letter based on Scrabble letter values.

    Raises:
    ValueError: If the input is not a string or contains non-alphabetic characters.
    """
    if not isinstance(letter, str) or len(letter) != 1 or not letter.isalpha():
        raise TypeError("Input parameter must be a single alphabetic character string")

    letter_score_map = {
        "E": 1, "A": 1, "I": 1, "O": 1, "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, 
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    letter = letter.upper()
    return letter_score_map.get(letter, 0)


def calculate_word_score(word: str) -> int:
    """
    Calculate the Score of a Given Word in Scrabble.

    This function takes a single word as input and calculates its score based on Scrabble's scoring rules. 
    Each letter in the word has a point value, and the function sums these values to get the total score of the word.

    Parameters:
    word (str): The word for which the score is to be calculated. The word should be a valid string 
                consisting of uppercase or lowercase alphabetic characters. It should not contain any spaces or special characters.

    Returns:
    int: The total score of the word based on Scrabble letter values.

    Raises:
    ValueError: If the input is not a string or contains non-alphabetic characters.
    """
    if not isinstance(word, str) or not word.isalpha():
        raise TypeError("Input parameter must be a string containing only alphabetic characters")

    return sum(get_letter_score(letter) for letter in word)
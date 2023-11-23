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
    if not isinstance(letter, str):
        raise TypeError("Input parameter to get_letter_score must be in str format")

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
    if not isinstance(word, str):
        raise TypeError("Input parameter to calculate_word_score must be in str format")

    score = 0
    letter_score_map = {
        1: ["E", "A", "I", "O", "N", "R", "T", "L", "S", "U"], 
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    for letter in word: 
        score += get_letter_score(letter)
    
    return letter
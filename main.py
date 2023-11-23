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

import random

NUMBER_OF_TILES = 7

def get_words(n: int) -> list:
    """
    Return a list of words based on words found in dictionary.txt. 

    Returns:
    valid_words (list): A list of valid words 
    """
    with open("dictionary.txt", "r") as file: 
        all_words = file.readlines()
    
    return [word.upper() for word in all_words if len(word) <= NUMBER_OF_TILES]


WORDS = get_words(NUMBER_OF_TILES)

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

def assign_tiles(n: int) -> list[str]:
    """
    Assign a set of random tiles (characters) to a player rack (list). 

    This function is responsible for randomly selecting and assigning seven tiles from the English alphabet 
    to a player's rack in a Scrabble game. The selection of tiles is based on the standard distribution of 
    letters in Scrabble, where certain letters are more common than others.

    Returns:
    rack (list[str]): A list containing seven characters, each representing a tile assigned to the player's rack.
    """
    bag = ["E"] * 12 + ["A", "I"] * 9 + ["O"] * 8 + ["N", "R", "T"] * 6 + ["L", "S", "U", "D"] * 4 + ["G"] * 3 + ["B", "C", "M", "P", "F", "H", "V", "W", "Y"] * 2 + ["K", "J", "X", "Q", "Z"]
    print(random.sample(bag, 7))
    return random.sample(bag, 7)

def get_valid_words(rack: list[str]) -> set:
    """
    Check if a Word is Valid Based on a Set of Tiles and a Dictionary.

    This function returns a list of valid words which can be formed formed from a specified set of seven tiles 
    and is a valid word according to the Scrabble dictionary. The validation is based on two criteria: 
    first, whether the word can be constructed from the provided tiles, and second, whether the word 
    exists in 'dictionary.txt', which contains a list of valid Scrabble words.

    Returns:
    valid_words (set): A set of valid words which can be formed formed from a specified set of seven tiles 
    """
    valid_words = set()
    for word in WORDS:
        word = word.strip().upper()
        temp_rack = rack.copy()
        
        for letter in word:
            if letter in temp_rack:
                temp_rack.remove(letter)
            else:
                break
        else:
            valid_words.add(word)

    return valid_words



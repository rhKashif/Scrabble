"""
Scrabble Game Test Module

This test module contains a suite of unit tests for the Scrabble game implemented in Python. 
It is designed to test the functionality of various components and functions defined in the 
main game module. These tests ensure the correctness of game logic, including word validation, 
score calculation and tile distribution.

The tests are organized by functionality, with each test case focusing on a specific aspect 
of the game. This organization helps in identifying and isolating bugs or issues in the codebase.

Note:
    It's important to keep the tests up-to-date with any changes in the game's logic or 
    functionality to maintain the reliability of the tests.

Author: Hassan Kashif
"""
import pytest

from main import get_letter_score, calculate_word_score, assign_tiles

def test_get_letter_score_correct_score():
    test_parameter = "G"
    expected_return = 2
    assert get_letter_score(test_parameter) == expected_return

def test_get_letter_score_invalid_parameter_type():
    test_parameter = []
    with pytest.raises(TypeError):
        get_letter_score(test_parameter)    

def test_get_letter_score_invalid_parameter_length():
    test_parameter = "INVALID PARAMETER"
    with pytest.raises(TypeError):
        get_letter_score(test_parameter) 

def test_get_letter_score_invalid_parameter_character():
    test_parameter = "2"
    with pytest.raises(TypeError):
        get_letter_score(test_parameter)      

def test_calculate_word_score_correct_score():
    test_parameter = "GUARDIAN"
    expected_return = 10
    assert calculate_word_score(test_parameter) == expected_return

def test_calculate_word_score_invalid_parameter():
    test_parameter = ["INVALID PARAMETER"]
    with pytest.raises(TypeError):
        calculate_word_score(test_parameter)

def test_assign_tiles():
    expected_return_length = 7
    assert len(assign_tiles()) == expected_return_length

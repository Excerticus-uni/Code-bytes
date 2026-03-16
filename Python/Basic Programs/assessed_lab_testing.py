import pytest
from assessed_lab_excercises import *

def test_calculator(num1, num2, operator):
    # Basic operations
    assert calculator(10, 5, "+") == 15
    assert calculator(10, 5, "-") == 5 
    assert calculator(10, 5, "*") == 50
    assert calculator(10, 5, "/") == 2.0 
    assert calculator(10, 5, ">") == True  
    assert calculator(10, 5, "<=") == False 
    # Erroneous values
    assert calculator(10, 0, "/") == 'Cannot Divide by zero!'
    assert calculator(10, 5, "$") == 'Invalid operator!' 

def test_max_of_three(num1, num2, num3):
    # your code
    return

def test_winning_numbers(winning_list, guessed_list):
    # your code
    return

def test_sum_of_evens(min_num, max_num):
    # your code
    return

def test_calculate_average(num_list):
    # your code
    return

def test_calculate_weekly_pay(hours_worked):
    # your code
    return


def test_is_prime(num):
    # your code
    return

def test_are_anagrams(word1, word2):
    # your code
    return

def test_count_vowels(input_string):
    # your code
    return

def test_sort_list(num_list):
    # your code
    return

def test_sum_of_digits(num):
    # your code
    return

def test_is_palindrome(input_string):
    # your code
    return

def test_password_strength(password):
    # your code
    return

def test_letter_grade(list_of_dictionary):
    # your code
    return

def test_maximum_gap(list1, list2):
    # your code
    return

def test_cipher_test(input_text, key):
    # your code
    return

def test_net_annual_incomde(gross_salary):
    # your code
    return

def test_my_split(my_str, sep):
    # your code
    return

def test_longest_repetition(text):
    # your code
    return

def test_closest_pair_under_budget(prices, budget):
    # your code
    return
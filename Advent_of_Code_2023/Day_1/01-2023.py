#!/usr/bin/env python3

from typing import List

"""
Solutions for Day 1
"""

def sum_of_calibration_values(input_data_string_list: List[str]) -> int:
    """
    Parses each string in list from start to end and end to start 
    Detects first digit in each direction and concatenates 
    Converts to int and increments total
    """
    total = 0
    for string in input_data_string_list:
        left_digit = ''
        right_digit = ''
        for char in string:
            if char.isdigit():
                left_digit = char
        for char in range(-1, -len(string) - 1, -1):
            if string[char].isdigit():
                right_digit = string[char]
        combined_digits = right_digit + left_digit
        total += int(combined_digits)
    return total

def part_1() -> None:
    """
    Solution for Part 1
    """
    input_data = '01-2023.txt'
    input_data_string_list = []

    with open(input_data) as lines:
        for line in lines:
            input_data_string_list.append(str(line).strip())

    print(f"Part 1: {sum_of_calibration_values(input_data_string_list)}")

def part_2() -> None:
    """
    Solution for Part 2
    """
    input_data = '01-2023.txt'
    input_data_string_list = []
    amended_string_list = []

    word_to_numeric_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    with open(input_data) as lines:
        for line in lines:
            input_data_string_list.append(str(line).strip())

    for string in input_data_string_list:
        for word, numeric in word_to_numeric_dict.items():
            if word in string:
                string = string.replace(word, f"{word}{numeric}{word}")
        amended_string_list.append(string)

    print(f"Part 2: {sum_of_calibration_values(amended_string_list)}")

if __name__ == "__main__":
    part_1()
    part_2()

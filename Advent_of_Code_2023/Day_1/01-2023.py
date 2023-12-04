#!/usr/bin/env python3

"""
Solutions for Day 1
"""


def sum_of_calibration_values():
    """
    Solution for Part 1
    """
    input_data = '01-2023.txt'
    # input_data = 'smalltest.txt'
    str_list = []
    total = 0

    with open(input_data) as lines:
        for line in lines:
            str_list.append(str(line).strip())

    for string in str_list:
        print(string)
        left_digit = ''
        right_digit = ''
        for char in string:
            if char.isdigit():
                left_digit = char
        for char in range(-1, -len(string) - 1, -1):
            if string[char].isdigit():
                right_digit = string[char]
        combined_digits = right_digit + left_digit
        print(f"Combined Digits: {combined_digits}")
        total += int(combined_digits)
    print(f"Total: {total}")

if __name__ == "__main__":
    sum_of_calibration_values()

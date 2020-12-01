#!/usr/bin/env python3

"""
Day 1: find the two/three entries in list that sum to the target sum and then
multiply those numbers together
e.g. num_list = [1721, 979, 366, 299,  675, 1456]
1721 + 299 = 2020
1721 * 299 = 514579
"""


def sum_two():
    """
    uses three numbers from the list
    prints indices, values and product of ints that sum to the target sum
    """
    input_data = '01-2020.txt'
    target_sum = 2020
    num_list = []

    with open(input_data) as lines:  # convert .txt into Python list of ints
        line = lines.readline()
        for line in lines:
            num_list.append(int(line.strip()))  # remove new lines, whitespace

    print("sum_two()")
    for x in range(len(num_list)):
        for y in range(len((num_list))):
            if x == y:  # skip identical indices
                continue
            if num_list[x] + num_list[y] == target_sum:
                print(f"indices: {x} {y}")
                print(f"values: {num_list[x]} {num_list[y]}")
                print(f"product: {num_list[x] * num_list[y]}")


def sum_three():
    """
    uses three numbers from the list
    prints indices, values and product of ints that sum to the target sum
    """
    input_data = '01-2020.txt'
    target_sum = 2020
    num_list = []

    with open(input_data) as lines:  # convert .txt into Python list of ints
        line = lines.readline()
        for line in lines:
            num_list.append(int(line.strip()))

    print("sum_three()")
    for x in range(len(num_list)):
        for y in range(len((num_list))):
            for z in range(len(num_list)):
                if x == y or x == z or y == z:  # skip identical indices
                    continue
                if num_list[x] + num_list[y] + num_list[z] == target_sum:
                    print(f"indices: {x} {y} {z}")
                    print(f"values: {num_list[x]} {num_list[y]} {num_list[z]}")
                    print(f"product: {num_list[x] * num_list[y] * num_list[z]}")


if __name__ == "__main__":
    sum_two()
    sum_three()

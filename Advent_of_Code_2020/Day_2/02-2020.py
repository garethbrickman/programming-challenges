#!/usr/bin/env python3

"""
Solutions for Day 2
"""


def validate_passwords():
    """
    Solution for Part 1
    """
    input_data = '02-2020.txt'
    valid = 0

    with open(input_data) as lines:
        for line in lines:
            count = 0
            line = line.split()
            line[0] = line[0].split('-')
            line[1] = line[1][:-1]

            for i in line[2]:
                if i == line[1]:
                    count += 1
            if int(line[0][0]) <= count <= int(line[0][1]):
                valid += 1
    print(valid)

def validate_passwords2():
    """
    Solution for Part 2
    """
    input_data = '02-2020.txt'

    with open(input_data) as _file:
        lines = _file.readlines()
    data = []
    for line in lines:
        _list = line.replace(":", "").strip().split(" ")
        data.append(_list)
    is_valid = 0
    for item in data:
        for idx, value in enumerate(item):
            if idx == 0:
                val = value.split("-")
                fPos = int(val[0])
                sPos = int(val[1])
            if idx == 1:
                char = value
            if idx == 2:
                pwd = value
        if pwd[fPos - 1] == char or pwd[sPos - 1] == char:
            is_valid += 1
        if pwd[fPos - 1] == char and pwd[sPos - 1] == char:
            is_valid -= 1
    print(is_valid)


if __name__ == "__main__":
    validate_passwords()
    validate_passwords2()

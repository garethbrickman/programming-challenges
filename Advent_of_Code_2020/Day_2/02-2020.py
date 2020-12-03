#!/usr/bin/env python3

"""
Day 2: count how many passwords in a given list are valid
based on given parameters

e.g.
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of
times a given letter must appear.
For example, 1-3 a means that the password must contain a at
least 1 time and at most 3 times.
In the above example, 2 passwords are valid.
"""


def validate_passwords():
    """
    uses three numbers from the list
    prints indices, values and product of ints that sum to the target sum
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


if __name__ == "__main__":
    validate_passwords()

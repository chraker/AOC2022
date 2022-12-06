import re
from textwrap import wrap


def part1():
    return length_to_end_of_first_unique_sequence(4)


def part2():
    return length_to_end_of_first_unique_sequence(14)


def length_to_end_of_first_unique_sequence(n):
    communication = open("data-day6.txt", "r").read()
    buffer = []
    count = 0
    for c in communication:
        count += 1
        buffer += c
        if len(buffer) > n:
            buffer.pop(0)
        if len(buffer) == n and len(set(buffer)) == len(buffer):
            break
    return count

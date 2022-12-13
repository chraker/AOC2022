from ast import literal_eval
from copy import deepcopy
from functools import cmp_to_key


def part1():
    packet_pairs = parse_package_pairs()
    valid_indexes = []
    for index, pair in enumerate(packet_pairs):
        if compare_package_pair(pair[0], pair[1]) == -1:
            valid_indexes.append(index + 1)
    return sum(valid_indexes)


def part2():
    packages = parse_packages()
    packages.append([[2]])
    packages.append([[6]])
    ordered = sorted(packages, key=cmp_to_key(lambda x, y: compare_package_pair(x, y)))
    decode_i_1 = ordered.index([[2]]) + 1
    decode_i_2 = ordered.index([[6]]) + 1
    return decode_i_1 * decode_i_2


def parse_packages():
    parsed_packets = []
    packets = open("data-day13.txt", "r").read().split('\n')
    while packets:
        candidate = packets.pop(0)
        if candidate != '\n' and candidate != '':
            parsed_packets.append(literal_eval(candidate))
    return parsed_packets


def parse_package_pairs():
    packet_pairs = []
    packets = open("data-day13.txt", "r").read().split('\n')
    while packets:
        packet1 = literal_eval(packets.pop(0))
        packet2 = literal_eval(packets.pop(0))
        packet_pairs.append([packet1, packet2])
        if packets:
            packets.pop(0)
    return packet_pairs


def compare_package_pair(a_i, b_i):
    a = deepcopy(a_i)
    b = deepcopy(b_i)
    a_is_list = type(a) == list
    b_is_list = type(b) == list
    if a_is_list and b_is_list:
        while a or b:
            if not a and not b:
                return 0
            if not a:
                return -1
            if not b:
                return 1
            result = compare_package_pair(a.pop(0), b.pop(0))
            if result != 0:
                return result
        return 0
    elif a_is_list:
        return compare_package_pair(a, [b])
    elif b_is_list:
        return compare_package_pair([a], b)
    return 0 if a is b else (-1 if int(a) < int(b) else 1)


if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

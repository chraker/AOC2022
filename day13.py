from ast import literal_eval


def part1():
    packet_pairs = parse_packages()

    valid_indexes = []
    for index, pair in enumerate(packet_pairs):
        if validate_package_pair(pair):
            valid_indexes.append(index + 1)
    return sum(valid_indexes)


def parse_packages():
    packet_pairs = []
    packets = open("data-day13.txt", "r").read().split('\n')
    while packets:
        packet1 = literal_eval(packets.pop(0))
        packet2 = literal_eval(packets.pop(0))
        packet_pairs.append([packet1, packet2])
        if packets:
            packets.pop(0)
    return packet_pairs


def validate_package_pair(pair):
    a, b = pair
    a_is_list = type(a) == list
    b_is_list = type(b) == list
    if a_is_list and b_is_list:
        while a or b:
            if not a and not b:
                return None
            if not a:
                return True
            if not b:
                return False
            result = validate_package_pair([a.pop(0), b.pop(0)])
            if result is not None:
                return result
        return None
    elif a_is_list:
        return validate_package_pair([a, [b]])
    elif b_is_list:
        return validate_package_pair([[a], b])
    return None if a is b else int(a) < int(b)


def part2():
    return 0


if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

def get_top_n_elves(elves_count):
    current_elf = 0
    top_elves = [0] * elves_count
    file_content = open("data-day1.txt", "r").read()
    for i in file_content.split('\n'):
        if i.isdigit():
            current_elf += int(i)
        else:
            min_carried_by_a_top_elf = min(top_elves)
            if current_elf > min_carried_by_a_top_elf:
                top_elves[top_elves.index(min_carried_by_a_top_elf)] = current_elf
            current_elf = 0
    return sum(top_elves)


def part1():
    return get_top_n_elves(1)


def part2():
    return get_top_n_elves(3)

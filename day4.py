def part1():
    file_content = open("data-day4.txt", "r").read()
    overlaps = 0
    for content in file_content.split('\n'):
        elf1, elf2 = content.split(',')
        if has_total_overlap(elf1, elf2):
            overlaps += 1
    return overlaps


def has_total_overlap(section_elf1, section_elf2):
    elf1_start, elf1_end = map(int, section_elf1.split('-'))
    elf2_start, elf2_end = map(int, section_elf2.split('-'))
    elf1_in_elf2 = elf1_start >= elf2_start and elf1_end <= elf2_end
    elf2_in_elf1 = elf1_start <= elf2_start and elf1_end >= elf2_end
    return elf1_in_elf2 or elf2_in_elf1


def part2():
    file_content = open("data-day4.txt", "r").read()
    overlaps = 0
    for content in file_content.split('\n'):
        elf1, elf2 = content.split(',')
        if has_overlap(elf1, elf2):
            overlaps += 1
    return overlaps


def has_overlap(section_elf1, section_elf2):
    elf1_start, elf1_end = map(int, section_elf1.split('-'))
    elf2_start, elf2_end = map(int, section_elf2.split('-'))
    elf1_left_of_elf2 = elf1_end < elf2_start
    elf1_right_of_elf2 = elf1_start > elf2_end
    return not (elf1_left_of_elf2 or elf1_right_of_elf2)

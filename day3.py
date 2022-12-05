from curses.ascii import isupper


def part1():
    file_content = open("data-day3.txt", "r").read()
    sum_priority = 0
    for content in file_content.split('\n'):
        compartment1, compartment2 = content[:len(content) // 2], content[len(content) // 2:]
        for entry in compartment1:
            if entry in compartment2:
                sum_priority += get_priority_for_item(entry)
                break
    return sum_priority


def part2():
    file_content = open("data-day3.txt", "r").read()
    lines = file_content.split('\n')
    total_badge_priority = 0
    while len(lines):
        elf1 = lines.pop(0)
        elf2 = lines.pop(0)
        elf3 = lines.pop(0)
        for entry in elf1:
            if entry in elf2 and entry in elf3:
                total_badge_priority += get_priority_for_item(entry)
                break
    return total_badge_priority


def get_priority_for_item(item):
    as_char = ord(item)
    return as_char - (38 if isupper(as_char) else 96)

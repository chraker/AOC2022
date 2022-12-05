import re
from textwrap import wrap


def part1():
    storage, commands = parse_input()
    updated_storage = apply_commands(commands, storage)
    return get_top_crates(updated_storage)


def part2():
    storage, commands = parse_input()
    updated_storage = apply_commands(commands, storage, True)
    return get_top_crates(updated_storage)


def parse_input():
    storage, commands = open("data-day5.txt", "r").read().split('\n\n')
    return get_storage(storage), get_commands(commands)


def get_storage(input):
    lines = input.split('\n')
    storage_size = int((len(lines[0]) + 1) / 4)
    storage = [[] for _ in range(storage_size)]
    for line in lines:
        entries = wrap(line, width=4, replace_whitespace=False, drop_whitespace=False)
        for stack, entry in enumerate(entries):
            for c in entry:
                if c.isalpha():
                    (storage[stack]).append(c)
    return storage


def get_commands(input):
    commands = []
    for content in input.split('\n'):
        amount, from_stack, to_stack = map(int, re.findall(r'\d+', content))
        commands.append([amount, from_stack - 1, to_stack - 1])
    return commands


def apply_commands(commands, storage, bulk=False):
    for command in commands:
        amount = command[0]
        from_stack = command[1]
        to_stack = command[2]
        if bulk:
            crates_to_move = storage[from_stack][:amount]
            storage[from_stack] = storage[from_stack][amount:]
            storage[to_stack] = crates_to_move + storage[to_stack]
        else:
            for i in range(amount):
                crate_to_move = storage[from_stack].pop(0)
                storage[to_stack].insert(0, crate_to_move)
    return storage


def get_top_crates(storage):
    top_crates = ''
    for stack in storage:
        top_crates += stack.pop(0)
    return top_crates

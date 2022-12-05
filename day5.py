import re


def create_storage():
    return [
        ['W', 'M', 'L', 'F'],
        ['B', 'Z', 'V', 'M', 'F'],
        ['H', 'V', 'R', 'S', 'L', 'Q'],
        ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
        ['L', 'S', 'W'],
        ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
        ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
        ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
        ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W'],
    ]


def part1():
    storage = create_storage()
    commands = get_commands()
    updated_storage = apply_commands(commands, storage)
    return get_top_crates(updated_storage)


def part2():
    storage = create_storage()
    commands = get_commands()
    updated_storage = apply_commands(commands, storage, True)
    return get_top_crates(updated_storage)


def get_commands():
    file_content = open("data-day5.txt", "r").read()
    commands = []
    for content in file_content.split('\n'):
        amount, from_stack, to_stack = map(int, re.findall(r'\d+', content))
        commands.append([amount, from_stack - 1, to_stack - 1])
    return commands


def apply_commands(commands, storage, bulk=False):
    for command in commands:
        amount = command[0]
        from_stack = command[1]
        to_stack = command[2]
        if bulk:
            pos_bottom_of_stack_to_move = len(storage[from_stack]) - amount
            crates_to_move = storage[from_stack][pos_bottom_of_stack_to_move:]
            storage[from_stack] = storage[from_stack][:pos_bottom_of_stack_to_move]
            storage[to_stack] += crates_to_move
        else:
            for i in range(amount):
                crate_to_move = storage[from_stack].pop()
                storage[to_stack].append(crate_to_move)
    return storage


def get_top_crates(storage):
    top_crates = ''
    for stack in storage:
        top_crates += stack.pop()
    return top_crates


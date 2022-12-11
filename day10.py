def part1():
    history_x = run_instructions_and_get_historic_x_register_values()
    return get_total_signal_strength([20, 60, 100, 140, 180, 220], history_x)


def part2():
    history_x = run_instructions_and_get_historic_x_register_values()
    return draw(history_x)


def run_instructions_and_get_historic_x_register_values():
    output = open("data-day10.txt", "r").read()
    queue = generate_execution_queue(output)
    return execute_queue(queue)


def generate_execution_queue(instructions):
    c = 0
    queue = []
    for line in instructions.split('\n'):
        if line == "noop":
            c += 1
            queue.append([c, 0])
        else:
            instruction, value = line.split(' ')
            if instruction == "addx":
                c += 2
                queue.append([c, int(value)])
    return queue


def execute_queue(queue):
    x = 1
    history_x = []
    while queue:
        x = execute_cycle(queue, x)
        history_x.append(x)
    return history_x


def execute_cycle(q, x):
    index_to_remove = []
    for index, item in enumerate(q):
        q[index][0] -= 1
        if not q[index][0]:
            x += q[index][1]
            index_to_remove.append(index)
    for index in index_to_remove:
        del q[index]
    return x


def get_total_signal_strength(cycles, register_history):
    signal_strength = 0
    for cycle in cycles:
        signal_strength += (register_history[cycle - 2] * cycle)
    return signal_strength


def draw(history_x):
    screen = '\n '
    for cycle in range(0, 239):
        if not (cycle+1) % 40 and cycle != 0:
            screen += '\n'
        screen += '#' if abs(history_x[cycle] - ((cycle+1) % 40)) < 2 else ' '
    return screen


if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

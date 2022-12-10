import time

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import waitforbuttonpress


def part1():
    visited = get_visited_locations(2)
    return len(get_unique_locations(visited))


def part2():
    visited = get_visited_locations(10)
    return len(get_unique_locations(visited))


def get_unique_locations(locations):
    return set(locations)


def get_visited_locations(rope_length, simulate=False):
    start = [0, 0]
    rope = [[0 for _ in range(2)] for _ in range(rope_length)]
    history = [tuple(start)]
    output = open("data-day9.txt", "r").read()
    movements = output.split('\n')

    if simulate:
        fig, ax = plt.subplots()
        plt.ion()
        l_body, = ax.plot(0, 0)
        l_head, = ax.plot(0, 0)
        l_tail, = ax.plot(0, 0)
        l_tail_history, = ax.plot(0, 0)
        ax.set_xlim([-25, 25])
        ax.set_ylim([-25, 25])
        plt.draw()

    for movement in movements:
        direction, length_str = movement.split(' ')
        length = int(length_str)
        for _ in range(0, length):
            rope[0] = move(rope[0], direction)
            for index, knot in enumerate(rope):
                if index != 0:
                    rope[index] = follow(rope[index - 1], knot, direction)
            history.append(tuple(rope[len(rope) - 1]))

            if simulate:
                x = np.array(list(map(lambda c: c[0], history)))
                y = np.array(list(map(lambda c: c[1], history)))
                l_tail_history.set_data(x, y)

                x = np.array(list(map(lambda c: c[0], rope)))
                y = np.array(list(map(lambda c: c[1], rope)))
                l_body.set_data(x, y)

                x = np.array(list(map(lambda c: c[0], rope[0:2])))
                y = np.array(list(map(lambda c: c[1], rope[0:2])))
                l_head.set_data(x, y)

                x = np.array(list(map(lambda c: c[0], rope[8:9])))
                y = np.array(list(map(lambda c: c[1], rope[8:9])))
                l_tail.set_data(x, y)

                plt.draw()
                plt.pause(0.1)

    if simulate:
        plt.show()
        plt.pause(100)
    return history


def move(knot, direction):
    if direction == 'U':
        return [knot[0], knot[1] + 1]

    if direction == 'D':
        return [knot[0], knot[1] - 1]

    if direction == 'R':
        return [knot[0] + 1, knot[1]]

    if direction == 'L':
        return [knot[0] - 1, knot[1]]


def follow(head, tail, direction):
    if head is tail:
        return tail
    is_right = head[0] - tail[0] > 1
    is_left = head[0] - tail[0] < -1
    is_top = head[1] - tail[1] > 1
    is_bottom = head[1] - tail[1] < -1
    if is_top:
        if not adjacent(head, tail):
            x = tail[0]
            y = tail[1] + 1
            return [get_adjacent(head[0], x), y]
    if is_bottom:
        if not adjacent(head, tail):
            x = tail[0]
            y = tail[1] - 1
            return [get_adjacent(head[0], x), y]

    if is_right:
        if not adjacent(head, tail):
            x = tail[0] + 1
            y = tail[1]
            return [x, get_adjacent(head[1], y)]

    if is_left:
        if not adjacent(head, tail):
            x = tail[0] - 1
            y = tail[1]
            return [x, get_adjacent(head[1], y)]
    return tail


def get_adjacent(target, current):
    return current if target == current else current + 1 if current < target else current - 1


def shares_row_or_column(head, tail):
    return head[0] == tail[0] or head[1] == tail[1]


def adjacent(T, H):
    return abs(T[0] - H[0]) <= 1 and abs(T[1] - H[1]) <= 1

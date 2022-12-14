from matplotlib import pyplot as plt

sand_start = tuple([500, 0])


def part1():
    rocks = get_rocks()
    sands, void = simulate(rocks)
    visualize(rocks, sands, void)
    return len(sands)


def part2():
    rocks = get_rocks()
    lowest_rock = min(map(lambda r: r[1], rocks))
    floor_level = lowest_rock - 2
    sands, void = simulate(rocks, floor_level)
    visualize(rocks, sands, floor_level=floor_level)
    return len(sands)


def visualize(rocks, sands, void=None, floor_level=None):
    plt.scatter(*zip(*rocks), s=2, marker="s")
    plt.scatter(*zip(*sands), s=1)
    plt.scatter(sand_start[0], sand_start[1] + 1)
    if type(void) is set:
        plt.scatter(*zip(*void), s=1, marker="x")
    elif floor_level is not None:
        left_most_rock = min(map(lambda r: r[0], rocks | sands))
        right_most_rock = max(map(lambda r: r[0], rocks | sands))
        plt.plot([left_most_rock, right_most_rock], [floor_level, floor_level])
    plt.show()


def simulate(rocks, floor=None):
    sands = set()
    void = set()
    sands_pured = 0
    while True:
        sands_pured += 1
        if sand_start in rocks | sands | void:
            break
        else:
            sand = sand_start
            sand_void_flow = False
            while True:
                next_sand_position = fall(sand, rocks | sands, floor)
                if floor is None and (is_falling_into_void(sand, rocks | sands) or next_sand_position in void):
                    sand_void_flow = True
                    break
                elif next_sand_position is sand:
                    break
                else:
                    sand = next_sand_position
            if sand_void_flow:
                void.add(sand)
            else:
                sands.add(sand)
    return sands, void


def fall(sand, blockers, floor):
    sx, sy = sand
    if floor is None or sy - 1 > floor:
        tile_below = tuple([sx, sy - 1])
        if tile_below not in blockers:
            return tile_below

        tile_below_left = tuple([sx - 1, sy - 1])
        if tile_below_left not in blockers:
            return tile_below_left

        tile_below_right = tuple([sx + 1, sy - 1])
        if tile_below_right not in blockers:
            return tile_below_right

    return sand


def is_falling_into_void(sand, blockers):
    x, y = sand
    for blocker in blockers:
        bx, by = blocker
        if bx == x and by < y:
            return False
    return True


def get_rocks():
    paths = open("data-day14.txt", "r").read().split('\n')
    rocks = set()
    for path in paths:
        s_start = None
        for segment in path.split('->'):
            if not s_start:
                s_start = segment
                continue
            else:
                s_end = segment
                xs, ys = map(int, s_start.split(','))
                xe, ye = map(int, s_end.split(','))

                while abs(xs - xe) >= 0:
                    while abs(ys - ye) >= 0:
                        rocks.add(tuple([xs, -ys]))
                        if ys == ye:
                            break
                        ys += 1 if ys < ye else -1
                    if xs == xe:
                        break
                    xs += 1 if xs < xe else -1
                s_start = s_end
    return rocks


if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

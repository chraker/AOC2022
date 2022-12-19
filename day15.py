import re

from matplotlib import pyplot as plt


def part1():
    target_y = 2000000
    sensors, beacons = get_sensors_and_beacons()
    minx = min(map(lambda s: s[0] - sensors[s], sensors.keys()))
    maxx = max(map(lambda s: s[0] + sensors[s], sensors.keys()))
    scanned = scan_range(sensors, [[minx, maxx], [target_y, target_y]])
    result = len(list(filter(lambda t: t[1] == target_y and t not in beacons, scanned)))

    plt.scatter(*zip(*scanned), s=4)
    plt.scatter(*zip(*beacons), s=4)
    for sensor, distance in sensors.items():
        plt.scatter(sensor[0], sensor[1], c="r")
    plt.show()
    return result


def part2():
    search_width = 4000000
    sensors, beacons = get_sensors_and_beacons([[0, search_width], [0, search_width]])
    edge_points = get_sensors_edge_points(sensors, [[0, search_width], [0, search_width]])

    # walk edges and find point that is not within distance of any sensors
    result = None
    for i, edge_point in enumerate(edge_points):
        ex, ey = edge_point
        result = edge_point
        for s in sensors.items():
            (x, y), distance = s
            if in_range(distance, x, y, ex, ey):
                result = False
                break
        if result:
            break

    # Plot stuff
    for sensor, distance in sensors.items():
        x, y = sensor
        plt.scatter(x, sensor[1], c="r")
        ex = [x - distance, x, x + distance, x, x - distance]
        ey = [y, y - distance, y, y + distance, y]
        plt.plot(ex, ey, c="b")
    plt.plot([0, 0, search_width, search_width, 0], [0, search_width, search_width, 0, 0], c='g')
    plt.scatter(*zip(*beacons), s=4)
    plt.scatter(result[0], result[1], s=12)
    plt.show()
    return result[0] * 4000000 + result[1]


def get_sensors_edge_points(sensors, r):
    edges = set()
    for s in sensors.items():
        edges = get_sensor_edge_points(s, r) | edges
    return edges


def get_sensor_edge_points(sensor, r):
    edges = set()
    (x, y), distance = sensor
    [[minx, maxx], [miny, maxy]] = r

    iy = y
    iy2 = y

    for ix in range(x - distance - 1, x):
        if minx <= ix <= maxx:
            if miny <= iy <= maxy:
                edges.add(tuple([ix, iy]))
            if miny <= iy2 <= maxy:
                edges.add(tuple([ix, iy2]))
        iy += 1
        iy2 -= 1

    iy = y - distance - 1
    iy2 = y + distance + 1
    for ix in range(x, x + distance + 2):
        if minx <= ix <= maxx:
            if miny <= iy <= maxy:
                edges.add(tuple([ix, iy]))
            if miny <= iy2 <= maxy:
                edges.add(tuple([ix, iy2]))
        iy += 1
        iy2 -= 1

    return edges

def scan_range(sensors, r):
    scanned = set()
    [[minx, maxx], [miny, maxy]] = r
    for x in range(minx, maxx):
        for y in range(miny, maxy) if miny != maxy else [miny]:
            r = scan(sensors, x, y)
            if r:
                scanned.add(r)
    return scanned


def scan(sensors, x, y):
    for index, ((sx, sy), distance) in enumerate(sensors.items()):
        if in_range(distance, sx, sy, x, y):
            return tuple([x, y])


def in_range(distance, sx, sy, x, y):
    return manhattan(sx, sy, x, y) <= distance


def manhattan(sx, sy, x, y):
    return abs(x - sx) + abs(y - sy)


def get_sensors_and_beacons(r=None):
    sensors = {}
    beacons = set()
    for sensor in open("data-day15.txt", "r").read().split('\n'):
        x, y, cbx, cby = map(int, re.findall(r'-?\d+', sensor))
        d = manhattan(x, y, cbx, cby)
        if r:
            [[minx, maxx], [miny, maxy]] = r
            reaches_in = in_range(d, x, y, minx, miny) or in_range(d, x, y, minx, maxy) or in_range(d, x, y, maxx,  miny) or in_range(d, x, y, maxx, maxy)
            inside = minx <= x <= maxx and miny <= y <= maxy
            if not reaches_in and not inside:
                continue
        sensors[tuple([x, y])] = d
        beacons.add(tuple([cbx, cby]))
    return sensors, beacons


if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

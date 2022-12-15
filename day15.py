import re

from matplotlib import pyplot as plt

def part1():
    target_y = 10
    sensors, beacons = get_sensors_and_beacons()
    minx = min(map(lambda s: s[0] - sensors[s], sensors.keys()))
    maxx = max(map(lambda s: s[0] + sensors[s], sensors.keys()))
    scanned = scan_range(sensors, [minx, maxx], [target_y, target_y])
    result = len(list(filter(lambda t: t[1] == target_y and t not in beacons, scanned)))

    plt.scatter(*zip(*scanned), s=4)
    plt.scatter(*zip(*beacons), s=4)
    for sensor, distance in sensors.items():
        plt.scatter(sensor[0], sensor[1], c="r")
    plt.show()
    return result


def part2():
    search_width = 4000000
    sensors, beacons = get_sensors_and_beacons()
    scanned = scan_range(sensors, [0, search_width], [0, search_width])
    candidates = set()
    for x in range(0, search_width):
        for y in range(0, search_width):
            candidates.add(tuple([x, y]))
    result = (candidates - scanned).pop()

    plt.scatter(*zip(*scanned), s=4)
    plt.scatter(*zip(*beacons), s=4)
    for sensor, distance in sensors.items():
        plt.scatter(sensor[0], sensor[1], c="r")
    plt.scatter(result[0], result[1], c="g")
    plt.show()

    return result[0] * result[1]



def scan_range(sensors, lx, ly):
    scanned = set()
    xmin, xmax = lx
    ymin, ymax = ly
    c = 0
    for x in range(xmin, xmax):
        print('{:.1%}'.format(c / (xmax * ymax)))
        if ymin == ymax:
            r = scan(sensors, x, ymin)
            if r:
                scanned.add(r)

        for y in range(ymin, ymax):
            c += 1
            r = scan(sensors, x, y)
            if r:
                scanned.add(r)
    return scanned



def scan(sensors, x, y):
    for index, (sensor, distance) in enumerate(sensors.items()):
        if (abs(x - sensor[0]) + abs(y - sensor[1])) <= distance:
            return tuple([x, y])


def get_sensors_and_beacons():
    sensors = {}
    beacons = set()
    for sensor in open("data-day15.txt", "r").read().split('\n'):
        x, y, cbx, cby = map(int, re.findall(r'-?\d+', sensor))
        distance = abs(x - cbx) + abs(y - cby)
        sensors[tuple([x, y])] = distance
        beacons.add(tuple([cbx, cby]))
    return sensors, beacons


if __name__ == '__main__':
    print(f'Result: {part2()}')

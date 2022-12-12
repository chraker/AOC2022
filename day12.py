from queue import PriorityQueue

import numpy as np


def part1():
    start_node, end_node, height_map = parse_height_map()
    paths = get_shortest_paths_from_node(start_node, parse_graph(height_map))
    return paths[end_node[0]][end_node[1]]


def part2():
    start_node, end_node, height_map = parse_height_map()
    paths = get_shortest_paths_from_node(end_node, parse_graph(height_map, True))

    path_lengths = []
    for start_location in get_nodes_of_elevation(height_map, 'a'):
        path_lengths.append(paths[start_location[0]][start_location[1]])

    return min(path_lengths)


def parse_height_map():
    rows = open("data-day12.txt", "r").read().split('\n')
    height_map = [[0 for _ in range(len(rows[0]))] for _ in range(len(rows))]
    start_node = None
    end_node = None

    for r_i, row in enumerate(rows):
        for c_i, elevation in enumerate(row):
            if elevation == 'S':
                elevation = 'a'
                start_node = [r_i, c_i]
            if elevation == 'E':
                elevation = 'z'
                end_node = [r_i, c_i]
            height_map[r_i][c_i] = elevation
    return start_node, end_node, height_map


def parse_graph(height_map, reverse=False):
    node_matrix = [[[] for _ in range(len(height_map[0]))] for _ in range(len(height_map))]
    for r_i, row in enumerate(height_map):
        for c_i, elevation in enumerate(row):
            candidates = []
            if r_i != 0:
                candidates.append([r_i - 1, c_i])
            if r_i is not len(height_map) - 1:
                candidates.append([r_i + 1, c_i])
            if c_i != 0:
                candidates.append([r_i, c_i - 1])
            if c_i is not len(row) - 1:
                candidates.append([r_i, c_i + 1])

            current_elevation = height_map[r_i][c_i]
            for candidate in candidates:
                target_elevation = height_map[candidate[0]][candidate[1]]
                if can_walk(current_elevation, target_elevation) if not reverse else can_walk(target_elevation, current_elevation):
                    node_matrix[r_i][c_i].append([candidate[0], candidate[1]])
    return node_matrix


def get_shortest_paths_from_node(source_node, node_matrix):
    shortest_path = [[float('inf') for _ in range(len(node_matrix[0]))] for _ in range(len(node_matrix))]
    shortest_path[source_node[0]][source_node[1]] = 0

    pq = PriorityQueue()
    pq.put((0, source_node))
    visited = []

    while not pq.empty():
        (_, current_node) = pq.get()
        visited.append(current_node)

        for neighbour in node_matrix[current_node[0]][current_node[1]]:
            if neighbour not in visited:
                old_length = shortest_path[neighbour[0]][neighbour[1]]
                new_length = shortest_path[current_node[0]][current_node[1]] + 1
                if new_length < old_length:
                    pq.put((new_length, neighbour))
                    shortest_path[neighbour[0]][neighbour[1]] = new_length
    return shortest_path


def can_walk(a, b):
    return elev_to_number(a) - elev_to_number(b) >= -1


def elev_to_number(elevation):
    return ord(elevation) - 96


def get_nodes_of_elevation(height_map, target_elevation):
    matches = []
    for r_i, row in enumerate(height_map):
        for c_i, elevation in enumerate(row):
            if elevation == target_elevation:
                matches.append([r_i, c_i])
    return matches


if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

def part1():
    return get_visible_trees(parse_trees())


def part2():
    return get_top_scenic_score(parse_trees())


def parse_trees():
    output = open("data-day8.txt", "r").read()
    lines = output.split('\n')
    trees = [[] for _ in range(len(lines))]
    for row_index, row in enumerate(lines):
        for column_index, tree in enumerate(row):
            trees[row_index].append(tree)
    return trees


def get_visible_trees(trees):
    visible_trees = 0
    for row_index, row in enumerate(trees):
        for column_index, tree in enumerate(row):
            if row_index == 0 or column_index == 0 or row_index == len(trees) - 1 or column_index == len(
                    row) - 1:
                visible_trees += 1
                continue
            left, right, top, bottom = directions(column_index, row_index, trees)
            visible = max(left) < tree or max(right) < tree or max(top) < tree or max(bottom) < tree

            if visible:
                visible_trees += 1
    return visible_trees


def get_top_scenic_score(trees):
    max_score = 0
    for row_index, row in enumerate(trees):
        for column_index, tree in enumerate(row):
            left, right, top, bottom = directions(column_index, row_index, trees)
            score = fov_length(left, tree) * fov_length(right, tree) * fov_length(top, tree) * fov_length(bottom, tree)

            if score > max_score:
                max_score = score
    return max_score


def directions(column_index, row_index, trees):
    row = trees[row_index]
    left_fov = list(reversed(row[:column_index]))
    right_fov = row[(column_index + 1):]
    column = [r[column_index] for r in trees]
    top_fov = list(reversed(column[:row_index]))
    bottom_fov = column[(row_index + 1):]
    return bottom_fov, left_fov, right_fov, top_fov


def fov_length(fov, tree):
    score = 0
    if fov:
        for t in fov:
            score += 1
            if t >= tree:
                break
    return score

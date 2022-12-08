def part1():
    return get_visible_trees(parse_trees())


def part2():
    return 0


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
            left = row[:column_index]
            right = row[(column_index + 1):]
            column = [r[column_index] for r in trees]
            top = column[:row_index]
            bottom = column[(row_index + 1):]
            visible = max(left) < tree or max(right) < tree or max(top) < tree or max(bottom) < tree

            if visible:
                visible_trees += 1
    return visible_trees

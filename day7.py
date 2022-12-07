import re
from textwrap import wrap

command_start = '$'


def part1():
    dir_sizes = calc_dir_sizes()
    small_dirs = get_dirs_of_size_or_below(dir_sizes, 100000)
    return sum(small_dirs.values())


def part2():
    return 0


def calc_dir_sizes():
    dirs = {}
    output = open("data-day7.txt", "r").read()
    current_path = []
    home_path = []
    for line in output.split('\n'):
        if line[0] == command_start:
            params = line[2:].split(' ')
            if params[0] == 'cd':
                if params[1] == '..':
                    current_path.pop()
                    continue
                if params[1] == '/':
                    current_path = home_path
                    continue
                current_path.append(params[1])

        else:
            o1, o2 = line.split(' ')
            if o1 != 'dir':
                temp_path = ""
                for path in current_path:
                    temp_path += ('/' + path)
                    if dirs.get(temp_path):
                        dirs[temp_path] += int(o1)
                    else:
                        dirs[temp_path] = int(o1)
    return dirs


def get_dirs_of_size_or_below(dirs, size):
    return dict((k, v) for k, v in dirs.items() if v <= size)

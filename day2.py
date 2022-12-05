shapes = ['A', 'B', 'C']
encryption_keys = ['X', 'Y', 'Z']


def part1():
    return play()


def play():
    score = 0
    file_content = open("data-day2.txt", "r").read()
    for round_entry in file_content.split('\n'):
        [shape_him, encryption_key] = round_entry.split(' ')
        shape_me = shapes[encryption_keys.index(encryption_key)]
        score += score_total(shape_him, shape_me)
    return score


def part2():
    return play_correctly()


def play_correctly():
    score = 0
    file_content = open("data-day2.txt", "r").read()
    for round_entry in file_content.split('\n'):
        [his_shape, encryption_key] = round_entry.split(' ')
        shape_me = select_shape_by_outcome(his_shape, encryption_key)
        score += score_total(his_shape, shape_me)
    return score


def select_shape_by_outcome(his_shape, encryption_key):
    if encryption_key == 'X':
        return get_loosing_shape(his_shape)
    if encryption_key == 'Y':
        return his_shape
    if encryption_key == 'Z':
        return get_winning_shape(his_shape)


def score_total(shape_him, shape_me):
    return score_match(shape_him, shape_me) + score_shape(shape_me)


def score_shape(shape_me):
    return shapes.index(shape_me) + 1


def score_match(his_shape, my_shape):
    shape_that_would_win_to_him = get_winning_shape(his_shape)

    if my_shape == his_shape:
        return 3
    if my_shape == shape_that_would_win_to_him:
        return 6
    else:
        return 0


def get_winning_shape(shape):
    return shapes[get_winning_shape_index(shapes.index(shape))]


def get_winning_shape_index(shape_index):
    shape_index = shape_index + 1
    return shape_index if shape_index < 3 else 0


def get_loosing_shape(shape):
    return shapes[get_loosing_shape_index(shapes.index(shape))]


def get_loosing_shape_index(shape_index):
    shape_index = shape_index - 1
    return shape_index if shape_index >= 0 else 2

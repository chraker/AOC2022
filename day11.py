from math import lcm


def part1():
    monkeys = parse_monkeys()
    monkeys = play_game(monkeys, 20)
    return get_monkeybusiness(monkeys)


def part2():
    monkeys = parse_monkeys()
    for monkey in monkeys:
        monkey.set_handle_worry(lambda w: w % lcm(*[m.divisible_by for m in monkeys]))
    monkeys = play_game(monkeys, 10000)
    return get_monkeybusiness(monkeys)


def parse_monkeys():
    monkey_input = open("data-day11.txt", "r").read().split('\n')
    monkeys = []

    while len(monkey_input):
        name_str, items_str, operation_str, test_str, if_true_str, if_false_str = monkey_input[:6]
        monkey_input = monkey_input[7:]

        items = list(map(int, items_str.split('Starting items: ').pop().split(',')))
        divisible_by = int(test_str.split('  Test: divisible by ').pop())
        success = int(if_true_str.split('throw to monkey ').pop())
        failure = int(if_false_str.split('throw to monkey ').pop())

        operator, value = operation_str.split('  Operation: new = old ').pop().split(' ')
        operation = make_operation_method(operator, value)

        monkeys.append(Monkey(name_str, items, operation, divisible_by, success, failure))

    return monkeys


def make_operation_method(operator, value):
    return lambda item: op[operator](item, item if value == 'old' else int(value))


def play_game(monkeys, rounds):
    for r in range(0, rounds):
        monkeys = play_round(monkeys)
    return monkeys


def play_round(monkeys):
    for monkey in monkeys:
        while monkey.items:
            item, receiver = monkey.throw()
            monkeys[receiver].items.append(item)
    return monkeys


def get_monkeybusiness(monkeys):
    inspections = sorted(list(map(lambda monkey: monkey.inspections, monkeys)))
    top1, top2 = inspections[-2:]
    return top1 * top2


class Monkey:
    def __init__(self, name, items, operation, divisible_by, success, failure):
        self.name = name
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.success = success
        self.failure = failure
        self.inspections = 0
        self.handle_worry = lambda i: i // 3

    def throw(self):
        item_to_throw = self.items[0]
        self.items = self.items[1:]
        item_to_throw = self.operation(item_to_throw)
        self.inspections += 1
        item_to_throw = self.handle_worry(item_to_throw)
        test = item_to_throw % self.divisible_by

        return item_to_throw, self.failure if test else self.success

    def set_handle_worry(self, handle_worry):
        self.handle_worry = handle_worry


op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y}

if __name__ == '__main__':
    print(f'Result: {part1()}')
    print(f'Result: {part2()}')

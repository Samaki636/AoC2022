import re


def read_file(file_name):
    with open(file_name) as infile:
        return infile.read().splitlines()


def start(infile, rounds_n, part_1):
    items = [list(map(int, re.findall(r'\d+', line))) for line in infile if 'Starting' in line]
    operators = [line.split()[-2] for line in infile if 'Operation' in line]
    operands = [line.split()[-1] for line in infile if 'Operation' in line]
    divisors = [line.split()[-1] for line in infile if 'Test' in line]
    true_monkeys = [line.split()[-1] for line in infile if 'true' in line]
    false_monkeys = [line.split()[-1] for line in infile if 'false' in line]
    inspect_counts = [0 for line in infile if "Monkey" in line]

    for _ in range(rounds_n):
        for monkey_index, monkey_items in enumerate(items):
            for item in monkey_items:
                inspect_counts[monkey_index] += 1
                operand = int(operands[monkey_index]) if operands[monkey_index] != 'old' else item
                item = item * operand if operators[monkey_index] == '*' else item + operand
                if part_1:
                    item = int(item / 3)
                else:
                    item %= 9699690  # Multiply all the prime divisors together to get this.
                target_monkeys = true_monkeys if item % int(divisors[monkey_index]) == 0 else false_monkeys
                items[int(target_monkeys[monkey_index])].append(item)
            monkey_items.clear()
    inspect_counts.sort()
    monkey_business = inspect_counts[-2] * inspect_counts[-1]
    print(monkey_business)


def main():
    infile = read_file("input02.txt")
    # start(infile, 20, True)
    start(infile, 10000, False)


main()

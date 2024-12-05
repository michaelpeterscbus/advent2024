import re


def part1(filename):
    with open(filename, 'r') as file:
        total = 0
        for line in file:
            matches = re.findall(r"(mul\(\d+,\d+\))", line)
            for match in matches:
                nums = match.replace('mul', '').replace('(', '').replace(')', '').split(',')
                total += int(nums[0]) * int(nums[1])
        print(total)

def part2(filename):
    input = open(filename, 'r').read().replace('\n', '')
    total = 0
    enabled = True
    matches = re.finditer(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)', input)

    for match in matches:
        do_indices = [m.start() for m in re.finditer(r'do\(\)', input[:match.start()])]
        dont_indices = [m.start() for m in re.finditer(r'don\'?t\(\)', input[:match.start()])]
        if do_indices and dont_indices:
            enabled = do_indices[-1] > dont_indices[-1]
        elif dont_indices:
            enabled = False
        elif do_indices:
            enabled = True

        if enabled:
            num1, num2 = map(int, match.groups())
            total += num1 * num2
    print(total)

part1('sample.txt')
part1('input.txt')

part2('sample2.txt')
part2('input.txt')
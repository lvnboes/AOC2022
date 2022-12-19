import os.path
from typing import List, Tuple

from utils import print_tr, timed


def read_input(uri: str) -> List[Tuple[str, int]]:
    result = []
    with open(file=uri, mode='rt') as input_file:
        for cycle in list(map(str.strip, input_file)):
            result.append(('noop', 0))
            if cycle.startswith('addx'):
                split_cycle = cycle.split(' ')
                result.append((split_cycle[0], int(split_cycle[1])))
    return result


def get_intervals(start: int, interval: int, x_positions: List[int]) -> List[int]:
    return list(map(lambda i: x_positions[i], range(start, len(x_positions), interval)))


def part_1(cycles: List):
    x_positions = [0]
    for i in range(1, len(cycles)):
        x_positions.append(x_positions[i - 1] + cycles[i][1])
        print(i)
        print(cycles[i])
        print(x_positions[i])
        print()
    print(x_positions)
    x_at_intervals = get_intervals(start=20, interval=40, x_positions=x_positions)
    print(x_at_intervals)
    return sum(x_at_intervals)


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Test.txt'
    day_10_input = read_input(uri=path)
    print_tr(1, timed(f=lambda: part_1(cycles=day_10_input)))


if __name__ == '__main__':
    main()

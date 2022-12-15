import os
from typing import List, Tuple


def read_input(uri: str) -> List[Tuple[str, str]]:
    with open(file=uri, mode='rt') as input_file:
        input_list = list(map(lambda x: x.replace('\n', ''), input_file))
    return list(map(lambda x: (x[:int(len(x)/2)], x[int(-len(x)/2):]), input_list))


def part_1(puzzle_input: List[Tuple[str, str]]) -> int:
    doubles = list(map(lambda x: list(set(x[0]).intersection(set(x[1])))[0], puzzle_input))
    return sum(list(map(lambda x: ord(x) - ord('A') + 27 if x.isupper() else ord(x) - ord('a') + 1, doubles)))


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day3.txt'
    day_3_input = read_input(uri=path)
    print(f'Part 1 : {part_1(puzzle_input=day_3_input)}')

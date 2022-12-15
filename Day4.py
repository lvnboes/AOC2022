import os.path
from typing import List
from utils import timed, print_tr


def read_input(uri: str) -> List[List[List[int]]]:
    with open(file=uri, mode='rt') as input_file:
        return list(map(
            lambda x: list(map(
                lambda y: list(map(
                    lambda z: int(z),
                    y.split('-')
                )),
                x.split(',')
            )),
            input_file
        ))


def part_1(puzzle_input: List[List[List[int]]]) -> int:
    return sum(list(map(
        lambda x: (max(x[0]) >= max(x[1]) and min(x[0]) <= min(x[1])
                   or max(x[0]) <= max(x[1]) and min(x[0]) >= min(x[1])),
        puzzle_input
    )))


def part_2(puzzle_input: List[List[List[int]]]) -> int:
    return sum(list(map(
        lambda x: (x[0][0] in range(x[1][0], x[1][1]+1)
                   or x[0][1] in range(x[1][0], x[1][1]+1)
                   or x[1][0] in range(x[0][0], x[0][1]+1)
                   or x[1][1] in range(x[0][0], x[0][1]+1)),
        puzzle_input
    )))


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day4.txt'
    day_4_input = read_input(uri=path)
    print_tr(1, timed(f=lambda: part_1(puzzle_input=day_4_input)))
    print_tr(2, timed(f=lambda: part_2(puzzle_input=day_4_input)))


if __name__ == '__main__':
    main()

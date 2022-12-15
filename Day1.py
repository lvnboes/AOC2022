import os.path
from typing import List
from utils import timed, print_tr


def read_input(uri: str) -> List[List[int]]:
    with open(file=uri, mode='rt') as input_file:
        puzzle_input_string = input_file.read()
    return list(map(lambda x: list(map(lambda y: int(y), x.split('\n'))), puzzle_input_string.split('\n\n')))


def get_cals_of_max_elves(puzzle_input: List[List[int]], max_elf_amount: int) -> int:
    return sum(sorted(list(map(lambda x: sum(x), puzzle_input)))[-max_elf_amount:])


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day1.txt'
    day_1_input = read_input(uri=path)
    print_tr(1, timed(f=lambda: get_cals_of_max_elves(puzzle_input=day_1_input, max_elf_amount=1)))
    print_tr(2, timed(f=lambda: get_cals_of_max_elves(puzzle_input=day_1_input, max_elf_amount=3)))


if __name__ == '__main__':
    main()

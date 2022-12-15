import os
from typing import List, Callable


def read_input(uri: str) -> List[List[str]]:
    with open(file=uri, mode='rt') as input_file:
        input_list = list(map(lambda x: x.replace('\n', '').split(' '), input_file))
    return input_list


def determine_outcome(x: int, y: int) -> int:
    if (x - y) == 0:
        return y + 3
    elif (x - y) in (1, -2):
        return y
    else:
        return y + 6


def determine_play(x: str, result: str) -> int:
    x = ord(x) - ord('A') + 1
    if result == 'X':
        return 3 if (x - 1) == 0 else (x - 1)
    elif result == 'Y':
        return x
    else:
        return 1 if (x + 1) == 4 else (x + 1)


def tourney_score(puzzle_input: List[List[str]], xyz_method: Callable[[str, str], int]) -> int:
    return sum(list(map(
        lambda rps: determine_outcome(x=ord(rps[0]) - ord('A') + 1, y=xyz_method(rps[0], rps[1])),
        puzzle_input
    )))


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day2.txt'
    day_2_input = read_input(uri=path)
    print(f'Part 1 : {tourney_score(puzzle_input=day_2_input, xyz_method=lambda x, y: ord(y) - ord("X") + 1)}')
    print(f'Part 2 : {tourney_score(puzzle_input=day_2_input, xyz_method=lambda x, y: determine_play(x=x, result=y))}')

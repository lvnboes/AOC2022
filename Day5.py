import copy
import os.path
from typing import List, Tuple, Callable
from utils import print_tr, timed


def read_input(uri: str) -> Tuple[List[List[str]], List[Tuple[int, ...]]]:
    with open(file=uri, mode='rt') as input_file:
        stacks, moves = tuple(map(lambda x: x.split('\n'), input_file.read().split('\n\n')))
        stacks = list(map(lambda x: x[1:-1], list(reversed(stacks))[1:]))
        stacks = list(map(
            lambda x: list(filter(lambda z: z != ' ', map(lambda y: y[x], stacks))),
            range(0, len(stacks[0]), 4)
        ))
        moves = list(map(
            lambda x: tuple(map(
                lambda y: int(y),
                x.replace('move ', '').replace(' from ', '|').replace(' to ', '|').split('|')
            )),
            moves
        ))
    return stacks, moves


def move_crates(
        stacks: List[List[str]],
        move: Tuple[int, ...],
        arrange_method: Callable[[List[str]], List[str]]
) -> List[List[str]]:
    stacks[move[2]-1] = stacks[move[2]-1] + arrange_method(stacks[move[1]-1][-move[0]:])
    stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
    return stacks


def solve(
        stacks: List[List[str]],
        moves: List[Tuple[int, ...]],
        arrange_method: Callable[[List[str]], List[str]]
) -> str:
    for move in moves:
        stacks = move_crates(stacks=stacks, move=move, arrange_method=arrange_method)
    return ''.join(list(map(lambda x: x[-1], stacks)))


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day5.txt'
    stacks, moves = read_input(uri=path)
    print_tr(1, timed(
        f=lambda: solve(stacks=copy.deepcopy(stacks), moves=moves, arrange_method=lambda x: list(reversed(x)))
    ))
    print_tr(2, timed(f=lambda: solve(stacks=copy.deepcopy(stacks), moves=moves, arrange_method=lambda x: list(x))))


if __name__ == '__main__':
    main()

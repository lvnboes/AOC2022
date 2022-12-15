import os
from typing import List, Callable
from utils import timed, print_tr


def read_input(uri: str) -> List[str]:
    with open(file=uri, mode='rt') as input_file:
        return list(map(lambda x: x.replace('\n', ''), input_file))


def compartmentalize(backpacks: List[str]) -> List[List[str]]:
    return list(map(lambda x: [x[:int(len(x)/2)], x[int(-len(x)/2):]], backpacks))


def group_by_number(number: int, backpacks: List[str], grouped_backpacks: List[List[str]]) -> List[List[str]]:
    if len(backpacks) >= number:
        grouped_backpacks.append(backpacks[:number])
        return group_by_number(number=number, backpacks=backpacks[number:], grouped_backpacks=grouped_backpacks)
    else:
        return grouped_backpacks


def find_common_item(x: str, xs: List[str]) -> str:
    if len(xs) > 0:
        return find_common_item(x=''.join(list(set(x).intersection(xs[0]))), xs=xs[1:])
    else:
        return x


def solve(backpacks: List[str], partitioned_method: Callable[[List[str]], List[List[str]]]) -> int:
    common_items = list(map(
        lambda backpack: find_common_item(x=backpack[0], xs=backpack[1:]),
        partitioned_method(backpacks)
    ))
    return sum(list(map(lambda x: ord(x) - ord('A') + 27 if x.isupper() else ord(x) - ord('a') + 1, common_items)))


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day3.txt'
    day_3_input = read_input(uri=path)
    print_tr(1, timed(f=lambda: solve(backpacks=day_3_input, partitioned_method=compartmentalize)))
    print_tr(2, timed(
        f=lambda: solve(
            backpacks=day_3_input,
            partitioned_method=lambda x: group_by_number(number=3, backpacks=x, grouped_backpacks=[])
        )
    ))


if __name__ == '__main__':
    main()

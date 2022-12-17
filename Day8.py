import os.path
from typing import List
from utils import print_tr, timed


def read_input(uri: str) -> List[List[int]]:
    with open(file=uri, mode='rt') as input_file:
        return list(map(lambda x: list(map(lambda y: int(y), [*x.strip()])), input_file))


def get_visibility(forrest: List[List[int]]) -> int:
    results = [
        [
            1 if (x in (0, len(forrest)-1) or y in (0, len(forrest[0])-1)) else 0 for y in range(len(forrest[0]))
        ] for x in range(len(forrest))
    ]
    max_top = forrest[0]
    max_bottom = forrest[len(forrest)-1]
    max_left = list(map(lambda x: x[0], forrest))
    max_right = list(map(lambda y: y[len(forrest[0])-1], forrest))
    for x in range(1, len(forrest)-1):
        for y in range(1, len(forrest[0])-1):
            if forrest[x][y] > max_top[y]:
                max_top[y] = forrest[x][y]
                results[x][y] = 1
            if forrest[x][y] > max_left[x]:
                max_left[x] = forrest[x][y]
                results[x][y] = 1
    for x in range(len(forrest)-2, 0, -1):
        for y in range(len(forrest[0])-2, 0, -1):
            if forrest[x][y] > max_bottom[y]:
                max_bottom[y] = forrest[x][y]
                results[x][y] = 1
            if forrest[x][y] > max_right[x]:
                max_right[x] = forrest[x][y]
                results[x][y] = 1
    return sum(list(map(lambda x: sum(x), results)))


def get_viewing_distance(forrest: List[List[int]], x: int, y: int):
    top_dist = bottom_dist = left_dist = right_dist = 0
    height = forrest[x][y]
    for a in range(x+1, len(forrest)):
        bottom_dist += 1
        if forrest[a][y] >= height:
            break
    for a in range(x-1, -1, -1):
        top_dist += 1
        if forrest[a][y] >= height:
            break
    for b in range(y+1, len(forrest[0])):
        right_dist += 1
        if forrest[x][b] >= height:
            break
    for b in range(y-1, -1, -1):
        left_dist += 1
        if forrest[x][b] >= height:
            break
    return top_dist * bottom_dist * left_dist * right_dist


def top_view(forrest: List[List[int]]) -> int:
    result = 0
    for x in range(0, len(forrest)):
        for y in range(0, len(forrest[0])):
            result = max(result, get_viewing_distance(forrest=forrest, x=x, y=y))
    return result


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day8.txt'
    day_8_input = read_input(path)
    print_tr(1, timed(lambda: get_visibility(forrest=day_8_input)))
    print_tr(2, timed(lambda: top_view(forrest=day_8_input)))


if __name__ == '__main__':
    main()

import os.path
from typing import List, Tuple
from utils import print_tr, timed


def read_input(uri: str) -> List[Tuple[str, int]]:
    with open(file=uri, mode='rt') as input_file:
        return list(map(lambda x: (x[0], int(x[2:].strip())), input_file))


def count_positions(directions: List[Tuple[str, int]], knot_count: int):
    tail_positions = [(0, 0)]
    knots = [(0, 0) for x in range(knot_count)]
    for direction in directions:
        for move in range(direction[1]):
            last_position = knots[0]
            if direction[0] == 'U':
                knots[0] = (last_position[0], last_position[1]-1)
            elif direction[0] == 'D':
                knots[0] = (last_position[0], last_position[1]+1)
            elif direction[0] == 'L':
                knots[0] = (last_position[0]-1, last_position[1])
            elif direction[0] == 'R':
                knots[0] = (last_position[0]+1, last_position[1])
            for i in range(1, len(knots)):
                if knots[i-1][0] - knots[i][0] > 1 and knots[i-1][1] - knots[i][1] > 1:
                    knots[i] = (knots[i][0] + 1, knots[i][1] + 1)
                elif knots[i-1][0] - knots[i][0] > 1 and knots[i-1][1] - knots[i][1] < -1:
                    knots[i] = (knots[i][0] + 1, knots[i][1] - 1)
                elif knots[i-1][0] - knots[i][0] < -1 and knots[i-1][1] - knots[i][1] > 1:
                    knots[i] = (knots[i][0] - 1, knots[i][1] + 1)
                elif knots[i-1][0] - knots[i][0] < -1 and knots[i-1][1] - knots[i][1] < -1:
                    knots[i] = (knots[i][0] - 1, knots[i][1] - 1)
                elif knots[i-1][0] - knots[i][0] > 1:
                    knots[i] = (knots[i][0] + 1, knots[i-1][1])
                elif knots[i-1][0] - knots[i][0] < -1:
                    knots[i] = (knots[i][0] - 1, knots[i-1][1])
                elif knots[i-1][1] - knots[i][1] > 1:
                    knots[i] = (knots[i-1][0], knots[i][1] + 1)
                elif knots[i-1][1] - knots[i][1] < -1:
                    knots[i] = (knots[i-1][0], knots[i][1] - 1)
                else:
                    break
            if knots[-1] not in tail_positions:
                tail_positions.append(knots[-1])
    return len(set(tail_positions))


def main():
    path = os.path.abspath(os.path.dirname(__file__)) + '/Day9.txt'
    day_9_input = read_input(uri=path)
    print_tr(1, timed(f=lambda: count_positions(directions=day_9_input, knot_count=2)))
    print_tr(2, timed(f=lambda: count_positions(directions=day_9_input, knot_count=10)))


if __name__ == '__main__':
    main()

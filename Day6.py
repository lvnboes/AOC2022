import os.path
from utils import timed, print_tr


def read_input(uri: str) -> str:
    with open(file=uri, mode='rt') as input_file:
        return input_file.read()


def solve(signal: str, marker_size: int) -> int:
    for x in range(marker_size-1, len(signal)):
        if len(set(signal[x-marker_size:x])) == marker_size:
            return x


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day6.txt'
    day_6_input = read_input(uri=path)
    print_tr(1, timed(f=lambda: solve(signal=day_6_input, marker_size=4)))
    print_tr(2, timed(f=lambda: solve(signal=day_6_input, marker_size=14)))


if __name__ == '__main__':
    main()

import os.path
from typing import List


def read_input(uri: str) -> List[str]:
    with open(file=uri, mode='rt') as input_file:
        return list(map(lambda x: x.replace('\n', ''), input_file))


def main():
    # path = os.path.dirname(os.path.abspath(__file__)) + '/Day7.txt'
    path = os.path.dirname(os.path.abspath(__file__)) + '/Test.txt'
    day_7_input = read_input(uri=path)
    for x in day_7_input:
        print(x)


if __name__ == '__main__':
    main()

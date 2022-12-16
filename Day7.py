import os.path
from typing import List, Dict


def read_input(uri: str) -> List[str]:
    with open(file=uri, mode='rt') as input_file:
        return list(map(lambda x: x.replace('\n', '').split(' '), input_file))


def create_file_structure(instructions: List[str]) -> Dict:
    current_level = ['["/"]']
    result = {"/": {'dirsize': 0}}
    name = 'result'
    for instruction in instructions:
        if instruction[0] == '$':
            if instruction[1] == 'cd':
                if instruction[2] == '..':
                    current_level = current_level[0:len(current_level)-1]
                elif instruction[2] == '/':
                    current_level = ['["/"]']
                else:
                    current_level.append(f'["{instruction[2]}"]')
        elif instruction[0] == 'dir':
            exec(f'{name}{"".join(current_level)}["{instruction[1]}"]={str({"dirsize": 0})}')
        else:
            for x in range(len(current_level)):
                exec(f'{name}{"".join(current_level[0:len(current_level)-x])}["dirsize"]+={int(instruction[0])}')
            exec(f'{name}{"".join(current_level)}["{instruction[1]}"]={int(instruction[0])}')
    return result


def main():
    # path = os.path.dirname(os.path.abspath(__file__)) + '/Day7.txt'
    path = os.path.dirname(os.path.abspath(__file__)) + '/Test.txt'
    day_7_input = read_input(uri=path)
    structure = create_file_structure(instructions=day_7_input)
    print(structure)


if __name__ == '__main__':
    main()

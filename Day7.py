import os.path
from typing import List, Dict

from utils import print_tr, timed


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


def sum_dir_sizes(file_structure: Dict):
    result = 0
    for x in file_structure.keys():
        if type(file_structure[x]) is dict:
            if file_structure[x]['dirsize'] < 100000:
                result += file_structure[x]['dirsize']
            result += sum_dir_sizes(file_structure=file_structure[x])
    return result


def find_dir_deletion(file_structure: Dict, total: int, disk_space: int, needed_space: int, result: int):
    for x in file_structure.keys():
        if type(file_structure[x]) is dict:
            if (file_structure[x]['dirsize'] >= result
                    or file_structure[x]['dirsize'] < (total - (disk_space - needed_space))):
                pass
            else:
                result = file_structure[x]['dirsize']
            result = find_dir_deletion(
                file_structure=file_structure[x],
                total=total,
                disk_space=disk_space,
                needed_space=needed_space,
                result=result
            )
    return result


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/Day7.txt'
    # path = os.path.dirname(os.path.abspath(__file__)) + '/Test.txt'
    day_7_input = read_input(uri=path)
    file_structure = create_file_structure(instructions=day_7_input)
    print_tr(1, timed(f=lambda: sum_dir_sizes(file_structure=file_structure)))
    print_tr(2, timed(f=lambda: find_dir_deletion(
        file_structure=file_structure,
        total=file_structure['/']['dirsize'],
        disk_space=70000000,
        needed_space=30000000,
        result=file_structure['/']['dirsize']
    )))


if __name__ == '__main__':
    main()

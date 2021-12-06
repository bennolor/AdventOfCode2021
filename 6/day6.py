from collections import defaultdict
from typing import Any


def grow_swarm(swarm: dict) -> dict:
    new_swarm: defaultdict[int, int] = defaultdict(int)
    for age in range(9):
        match age:
            case 0:
                new_swarm[6] += swarm[0]
                new_swarm[8] += swarm[0]
            case x if x > 0:
                new_swarm[age - 1] += swarm[age]
    return new_swarm


def get_swarm_from_my_input(my_input: str) -> dict:
    swarm_list = [int(x) for x in my_input.split(',')]
    return {
        0: swarm_list.count(0),
        1: swarm_list.count(1),
        2: swarm_list.count(2),
        3: swarm_list.count(3),
        4: swarm_list.count(4),
        5: swarm_list.count(5),
        6: swarm_list.count(6),
        7: swarm_list.count(7),
        8: swarm_list.count(8),
    }


def solution1(my_input: str) -> int:
    swarm = get_swarm_from_my_input(my_input)
    for x in range(80):
        swarm = grow_swarm(swarm)
    result = 0
    for key, value in swarm.items():
        result += value
    return result

def solution2(my_input: str) -> int:
    swarm = get_swarm_from_my_input(my_input)
    for x in range(256):
        swarm = grow_swarm(swarm)
    result = 0
    for key, value in swarm.items():
        result += value
    return result


if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        lanternfish_swarm = in_file.readline()

    print(f'after 80 days there are {solution1(lanternfish_swarm)} fishes')

    print(f"After 256 Days there are {solution2(lanternfish_swarm)} fishes")

import statistics


def get_crab_sub_position(in_str: str) -> list:
    return [int(x) for x in in_str.split(',')]


def calc_fuel_req(start: int, goal: int) -> int:
    return abs(start - goal)

def calc_fuel_crabgenieering(start:int, goal:int):
    return sum(range(1, abs(start-goal)+1))


def solution1(puzzle_input: str) -> int:
    pos_list = get_crab_sub_position(puzzle_input)
    goal_pos = int(statistics.median(pos_list))

    total_fuel = 0
    for crab_sub in pos_list:
        total_fuel += calc_fuel_req(crab_sub, goal_pos)

    return total_fuel


def solution2(puzzle_input: str) -> int:
    pos_list = get_crab_sub_position(puzzle_input)
    goal_pos = round(sum(pos_list)/len(pos_list)) # FUCK THIS. The  result here pre rounding is 489.501 Round gets 490. Advent of Code wants 489

    total_fuel = 0
    for crab_sub in pos_list:
        total_fuel += calc_fuel_crabgenieering(crab_sub, goal_pos)

    return total_fuel


if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        puzzle_input = in_file.readline()

    print(f'The Crabs need {solution1(puzzle_input)} fuel to line up')
    print(f'The Crabs need {solution2(puzzle_input)} fuel to line up using their crabsubs')

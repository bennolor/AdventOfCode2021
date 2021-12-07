import statistics


def get_crab_sub_position(in_str: str) -> list:
    return [int(x) for x in in_str.split(',')]


def solution1(puzzle_input: str) -> int:
    pos_list = get_crab_sub_position(puzzle_input)
    goal_pos = int(statistics.median(pos_list))

    return sum([abs(x - goal_pos) for x in pos_list])


def solution2(puzzle_input: str) -> int:
    pos_list = get_crab_sub_position(puzzle_input)
    # FUCK THIS. The  result here pre rounding is 489.501 Round gets 490. Advent of Code wants 489
    # goal_pos = round(sum(pos_list)/len(pos_list))

    # I did NOT come up with this. But I was frustrated that my solution was 1 off.
    goal_pos = round((sum(pos_list)/len(pos_list)) + ((len(pos_list) - 2 * len([x for x in pos_list if x < (sum(pos_list)/len(pos_list))]))/(2*len(pos_list))))


    return sum([sum(range(1, abs(x-goal_pos)+1)) for x in pos_list])


if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        puzzle_input = in_file.readline()

    print(f'The Crabs need {solution1(puzzle_input)} fuel to line up')
    print(f'The Crabs need {solution2(puzzle_input)} fuel to line up using their crabsubs')

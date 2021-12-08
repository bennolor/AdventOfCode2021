import shlex


def parse_input(puzzle_input: list) -> list:
    return [[y.split() for y in x] for x in [x.split(' | ') for x in puzzle_input]]


def get_seven_segment_digit(seg_str: str) -> int:
    pass


def solution1(puzzle_input: list) -> int:
    print(puzzle_input)
    puzzle_input = parse_input(puzzle_input)
    result = 0
    for line in puzzle_input:
        sig_in, sig_out = line
        for seg_sig in sig_out:
            match len(seg_sig):
                case 2 | 4 | 3 | 7:
                    result += 1

    return result


def solution2(puzzle_input: list) -> int:
    pass


if __name__ == '__main__':
    with open('in.txt', 'r') as input_file:
        my_input = input_file.readlines()
    print(f'In the Output the digits \'1,4,7,8\' appear {solution1(my_input)} times')
import itertools
import shlex


def parse_input(puzzle_input: list) -> list:
    return [[y.split() for y in x] for x in [x.split(' | ') for x in puzzle_input]]


def get_seven_segment_digit(signal_list: list) -> dict:
    segment_dict = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set(),
        9: set(),
    }
    simple_segments = {
        2: 1,
        4: 4,
        3: 7,
        7: 8,
    }
    for signal in itertools.chain(signal_list[0], signal_list[1]):
        match len(signal):
            case 2 | 4 | 3 | 7:
                segment_dict[simple_segments[len(signal)]] = set(signal)
            case 5 | 6:
                pass
            case _:
                raise ValueError(f"Revieved Signal {signal} with unexpected  Length {len(signal)} ")
    for signal in itertools.chain(signal_list[0], signal_list[1]):
        match len(signal):
            case 2 | 4 | 3 | 7:
                pass
            case 5:
                if len(segment_dict[7].intersection(signal)) == 3:
                    segment_dict[3] = set(signal)
                elif len(segment_dict[4].intersection(signal)) == 3:
                    segment_dict[5] = set(signal)
                else:
                    segment_dict[2] = set(signal)
            case 6:
                if len(segment_dict[4].intersection(signal)) == 4:
                    segment_dict[9] = set(signal)
                elif len(segment_dict[7].intersection(signal)) == 3:
                    segment_dict[0] = set(signal)
                else:
                    segment_dict[6] = set(signal)
            case _:
                raise ValueError(f"Revieved Signal {signal} with unexpected  Length {len(signal)} ")

    return segment_dict


def sig_to_num(sig_dict: dict, singal: str) -> int:
    for key, value in sig_dict.items():
        if not value.symmetric_difference(singal):
            return key
    raise KeyError(f'could not find signal \'{singal}\' in \n{sig_dict}')


def solution1(puzzle_input: list) -> int:
    # This part in one Line(dont do this):
    # return sum([len([y for y in x if len(y) in [2,4,3,7]]) for x in ([x[1] for x in [[y.split() for y in x] for x in [x.split(' | ') for x in puzzle_input]]])])
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
    puzzle_input = parse_input(puzzle_input)
    result = 0
    for line in puzzle_input:
        segment_dict = get_seven_segment_digit(line)
        sig_in, sig_out = line
        current_num = ""
        for seg_sig in sig_out:
            current_num += str(sig_to_num(segment_dict, seg_sig))
        result += int(current_num)

    return result


if __name__ == '__main__':
    with open('in.txt', 'r') as input_file:
        my_input = input_file.readlines()
    print(f'In the Output the digits \'1,4,7,8\' appear {solution1(my_input)} times')
    print(f'The Sum of all outputs is {solution2(my_input)}')

def validate_line(line: str):
    bracket_dict = {
        '<': '>',
        '(': ')',
        '[': ']',
        '{': '}',
    }
    opened_brackets = []
    for char in line.rstrip():
        if char in bracket_dict.keys():
            opened_brackets.append(char)
        else:
            if bracket_dict[opened_brackets.pop()] == char:
                pass
            else:
                return char

    return False


def solution1(puzzle_input: list)->int:
    fails = []
    for line in puzzle_input:
        if failed_bracket := validate_line(line):
            fails.append(failed_bracket)

    point_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return sum([point_dict[x] for x in fails])


if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        aoc_in = in_file.readlines()

    print(f'The total Syntax error Score is {solution1(aoc_in)}')

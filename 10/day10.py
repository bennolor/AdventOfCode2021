import math


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


def repair_line(line: str):
    bracket_dict = {
        '<': '>',
        '(': ')',
        '[': ']',
        '{': '}',
    }
    brackets = []
    for char in line.rstrip():
        if char in ['(', '[', '{', '<']:
            brackets.append(char)
        elif char in [')', ']', '}', '>']:
            if char == bracket_dict[brackets.pop()]:
                pass
            else:
                raise ValueError
        else:
            raise ValueError

    brackets.reverse()
    missing_brackets = []
    for bracket in brackets:
        missing_brackets.append(bracket_dict[bracket])

    return missing_brackets


def get_score(l: list):
    score_dict = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    r = 0
    for c in l:
        r *= 5
        r += score_dict[c]
    return r


def solution1(puzzle_input: list) -> int:
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


def solution2(puzzle_input: list) -> int:
    fix_brackets = []
    for line in puzzle_input:
        if not validate_line(line):
            fix_brackets.append(repair_line(line))

    scores = [get_score(x) for x in fix_brackets]

    if len(scores) % 2 == 0:
        raise ValueError

    scores.sort()

    return scores[math.floor(len(scores) / 2)]


if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        aoc_in = in_file.readlines()

    print(f'The total Syntax error Score is {solution1(aoc_in)}')
    print(f'The score of the one in the middle is {solution2(aoc_in)} ')

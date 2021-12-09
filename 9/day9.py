def parse_input(puzzle_input: list) -> list:
    return [[y for y in x.rstrip()] for x in puzzle_input]


def get_low_points(height_map: list) -> list:
    low_points = []
    for i, row in enumerate(height_map):
        for j, cell in enumerate(row):
            # This all could be optimized by calling it in the outer loop but I honestly could not care less,
            # as in most cases it should not reach the elif anyways, due to the edges always growing slower
            # than the edges and the corners being a constant 4

            # are we somewhere in the middle?
            if i and j and i != len(height_map) - 1 and j != len(row) - 1:
                if all(int(x) > int(cell) for x in
                       [height_map[i - 1][j], height_map[i + 1][j], row[j - 1], row[j + 1]]):
                    low_points.append((cell, i, j))
            # are we on the top side?
            elif not i and j not in [0, len(row) - 1]:
                if all(int(x) > int(cell) for x in [height_map[i + 1][j], row[j - 1], row[j + 1]]):
                    low_points.append((cell, i, j))
            # are we on the bottom side?
            elif i == len(height_map) - 1 and j not in [0, len(row) - 1]:
                if all(int(x) > int(cell) for x in [height_map[i - 1][j], row[j - 1], row[j + 1]]):
                    low_points.append((cell, i, j))
            # are we on the left side?
            elif i not in [0, len(height_map) - 1] and not j:
                if all(int(x) > int(cell) for x in
                       [height_map[i - 1][j], height_map[i + 1][j], row[j + 1]]):
                    low_points.append((cell, i, j))
            # are we on the right side?
            elif i not in [0, len(height_map) - 1] and j == len(row) - 1:
                if all(int(x) > int(cell) for x in
                       [height_map[i - 1][j], height_map[i + 1][j], row[j - 1]]):
                    low_points.append((cell, i, j))
            # are we in the top left corner?
            elif not i and not j:
                if all(int(x) > int(cell) for x in [height_map[i + 1][j], row[j + 1]]):
                    low_points.append((cell, i, j))
            # are we in the top right corner?
            elif not i and j == len(row) - 1:
                if all(int(x) > int(cell) for x in [height_map[i + 1][j], row[j - 1]]):
                    low_points.append((cell, i, j))
            # are we in the bottom left corner?
            elif i == len(height_map) - 1 and not j:
                if all(int(x) > int(cell) for x in [height_map[i - 1][j], row[j + 1]]):
                    low_points.append((cell, i, j))
            # are we in the bottom right corner?
            elif i == len(height_map) - 1 and j == len(row) - 1:
                if all(int(x) > int(cell) for x in [height_map[i - 1][j], row[j - 1]]):
                    low_points.append((cell, i, j))

    return low_points


def solution1(puzzle_input: list) -> int:
    parsed_puzzle_input = parse_input(puzzle_input)
    low_points = get_low_points(parsed_puzzle_input)
    print(low_points)
    low_points = map(lambda x: int(x[0]) + 1, low_points)

    return sum(low_points)


def solution2(puzzle_input: list) -> int:
    pass


if __name__ == '__main__':
    with open('in.txt', 'r') as input_file:
        aoc_input = input_file.readlines()

    print(f'the sum of the risk level is {solution1(aoc_input)}')

from functools import reduce


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


def validate_coord(heightmap: list, coord: tuple) -> bool:
    return len(heightmap) - 1 >= coord[1] >= 0 and len(heightmap[0]) - 1 >= coord[2] >= 0


def basin_propagator(coord: tuple, heightmap: list, basin_coords=None) -> set():
    if basin_coords is None:
        basin_coords = set()

    basin_coords.add(coord)
    # check below
    if validate_coord(heightmap, (0, coord[1] + 1, coord[2])):
        new_coord = (heightmap[coord[1] + 1][coord[2]], coord[1] + 1, coord[2])
        if new_coord[0] >= coord[0] and new_coord not in basin_coords and new_coord[0] != '9':
            basin_coords = basin_propagator(new_coord, heightmap, basin_coords)
    # check above
    if validate_coord(heightmap, (0, coord[1] - 1, coord[2])):
        new_coord = (heightmap[coord[1] - 1][coord[2]], coord[1] - 1, coord[2])
        if new_coord[0] >= coord[0] and new_coord not in basin_coords and new_coord[0] != '9':
            basin_coords = basin_propagator(new_coord, heightmap, basin_coords)
    # check right
    if validate_coord(heightmap, (0, coord[1], coord[2] + 1)):
        new_coord = (heightmap[coord[1]][coord[2] + 1], coord[1], coord[2] + 1)
        if new_coord[0] >= coord[0] and new_coord not in basin_coords and new_coord[0] != '9':
            basin_coords = basin_propagator(new_coord, heightmap, basin_coords)
    # check left
    if validate_coord(heightmap, (0, coord[1], coord[2] - 1)):
        new_coord = (heightmap[coord[1]][coord[2] - 1], coord[1], coord[2] - 1)
        if new_coord[0] >= coord[0] and new_coord not in basin_coords and new_coord[0] != '9':
            basin_coords = basin_propagator(new_coord, heightmap, basin_coords)

    return basin_coords


def get_basins(heightmap: list):
    low_points = get_low_points(heightmap)
    basins = []
    for low_point in low_points:
        basins.append(basin_propagator(low_point, heightmap))
    return basins


def solution1(puzzle_input: list) -> int:
    parsed_puzzle_input = parse_input(puzzle_input)
    low_points = get_low_points(parsed_puzzle_input)
    low_points = map(lambda x: int(x[0]) + 1, low_points)

    return sum(low_points)


def solution2(puzzle_input: list) -> int:
    parsed_puzzle_input = parse_input(puzzle_input)

    basins = get_basins(parsed_puzzle_input)
    basins = [len(basin) for basin in basins]
    basins.sort(reverse=True)

    # why not 'math.prod(basins[0:3])'? Dunno
    return reduce((lambda x, y: x * y), basins[0:3])


if __name__ == '__main__':
    with open('in.txt', 'r') as input_file:
        aoc_input = input_file.readlines()

    print(f'the sum of the risk level is {solution1(aoc_input)}')
    print(f'The sizes of the 3 largest Basins multiplied together is {solution2(aoc_input)}')

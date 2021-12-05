import collections
import math

if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        vent_vectors = [[x[0].split(','), x[1].split(',')] for x in map(lambda x: x.split(' -> '), in_file.readlines())]
        vent_vectors = [[[int(x[0][0]), int(x[0][1])], [int(x[1][0]), int(x[1][1])]] for x in vent_vectors]
    vent_coords = []

    for vent_vector in vent_vectors:
        if vent_vector[0][0] == vent_vector[1][0]:
            helper_list = [vent_vector[0][1], vent_vector[1][1]]
            helper_list.sort()
            for y_coord in range(helper_list[0], helper_list[1] + 1):
                vent_coords.append((vent_vector[0][0], y_coord))
        elif vent_vector[0][1] == vent_vector[1][1]:
            helper_list = [vent_vector[0][0], vent_vector[1][0]]
            helper_list.sort()
            for x_coord in range(helper_list[0], helper_list[1] + 1):
                vent_coords.append((x_coord, vent_vector[0][1]))

    duplicate_coords = [x for x, y in collections.Counter(vent_coords).items() if y > 1]
    print(f"There are {len(duplicate_coords)} overlapping coordinates with more than 1 vent if considering only horizontal and vertical vents")

    for vent_vector in vent_vectors:
        vector_start = vent_vector[0]
        vector_end = vent_vector[1]
        if not vector_start[0] == vector_end[0] and not vector_start[1] == vector_end[1]:

            if vector_start[0] > vector_end[0] and vector_start[1] > vector_end[1]:
                for step in range(0, abs(vector_start[0] - vector_end[0]) + 1):
                    coord = (vector_end[0]+step, vector_end[1]+step)
                    vent_coords.append((vector_end[0]+step, vector_end[1]+step))

            elif vector_start[0] > vector_end[0] and vector_start[1] < vector_end[1]:
                for step in range(0, abs(vector_start[0] - vector_end[0]) + 1):
                    vent_coords.append((vector_end[0]+step, vector_end[1]-step))

            elif vector_start[0] < vector_end[0] and vector_start[1] > vector_end[1]:
                for step in range(0, abs(vector_start[0] - vector_end[0]) + 1):
                    vent_coords.append((vector_start[0]+step, vector_start[1]-step))

            elif vector_start[0] < vector_end[0] and vector_start[1] < vector_end[1]:
                for step in range(0, abs(vector_start[0] - vector_end[0]) + 1):
                    vent_coords.append((vector_start[0]+step, vector_start[1]+step))

    duplicate_coords = [x for x, y in collections.Counter(vent_coords).items() if y > 1]
    print(f"There are {len(duplicate_coords)} overlapping coordinates with more than 1 vent if we considering the vents at an 45 Degree Angle too")






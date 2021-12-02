if __name__ == '__main__':
    with open("day2in.txt", "r") as my_in:
        course = [(x[0], int(x[1])) for x in list(map(lambda x: x.split(), my_in.readlines()))]

    h_pos = 0
    depth = 0

    for step in course:
        match step[0]:
            case "forward":
                h_pos += step[1]
            case "up":
                depth -= step[1]
            case "down":
                depth += step[1]

    print(f"We have arrived at a horizontal position of {h_pos} and our current depth is {depth}. The Answer is thus {h_pos*depth}")

if __name__ == '__main__':
    x = 0
    with open("a_in.txt", "r") as my_in:
        depth_list = list(map(lambda x: int(x), my_in.readlines()))

    for i in range(len(depth_list)):
        window_one_start = i
        if (sum(depth_list[i:i + 3])) < (sum(depth_list[i + 1:i + 4])):
            x += 1

    print(f"found {x} instances where the following window was bigger")

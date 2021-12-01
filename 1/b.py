if __name__ == '__main__':
    my_list = []
    x = 0
    with open("a_in.txt", "r") as my_in:
        for line in my_in:
            my_list.append(int(line))

    for i in range(len(my_list)):
        window_one_start = i
        if (sum(my_list[i:i + 3])) < (sum(my_list[i + 1:i + 4])):
            x += 1
    print(f"found {x} instances where the following window was bigger")

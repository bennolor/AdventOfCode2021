if __name__ == '__main__':
    with open("a_in.txt", "r") as my_in:
        depth_list = list(map(lambda x: int(x), my_in.readlines()))

    result = [sum(depth_list[i:i+3]) < sum(depth_list[i+1:i+4]) for i in range(len(depth_list))].count(True)
    print(f"found {result} instances where the following window was bigger")

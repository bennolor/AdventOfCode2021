import itertools

if __name__ == '__main__':
    with open("a_in.txt", "r") as my_in:
        depth_list = list(map(lambda x: int(x), my_in.readlines()))

    result = list(map(lambda a: a[0]<a[1], list(itertools.pairwise(depth_list)))).count(True)
    print(f"There are {result} measurements that are larger than the previous one")

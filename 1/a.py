if __name__ == '__main__':
    a = float("inf")
    b = 0
    x = 0
    with open("a_in.txt","r") as my_in:
        for line in my_in:
            b = int(line)
            if a < b:
                x += 1
            a = b
    print(f"There are {x} measurements that are larger than the previous one")

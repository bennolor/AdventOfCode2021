import math

if __name__ == '__main__':
    with open("in.txt", "r") as input_file:
        numbers = list(map(lambda x: x.rstrip(), input_file.readlines()))

        binary_len = len(numbers[0])

    def check_if_high_weighted(nums: list) -> bool:
        x = 0
        num_breakpoint = math.ceil(len(nums) / 2)
        for num in nums:
            if int(num):  # taking advantage of the auto casting of int 1 and int 0 to bool
                x += 1
                if x >= num_breakpoint:  # should never be larger but ehh might as well implement it like this
                    return True
        return False

    def iter_over_numbers(nums: list, nlen:int) -> str:
        out = ""
        for i in range(nlen):
            if check_if_high_weighted([x[i] for x in nums]):
                out += "1"
            else:
                out += "0"
        return out

    gamma_s = iter_over_numbers(numbers, binary_len)
    epsilon_s = "".join(["1" if x == "0" else "0" for x in gamma_s])
    print(f"Gamma rate is {gamma_s}, Epsilon Rate is {epsilon_s}. Power consumption is thus {int(gamma_s, 2) * int(epsilon_s, 2)}")

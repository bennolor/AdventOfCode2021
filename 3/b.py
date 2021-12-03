import math

if __name__ == '__main__':
    with open("in.txt", "r") as input_file:
        numbers = list(map(lambda x: x.rstrip(), input_file.readlines()))

        bin_len = len(numbers[0])


    def check_if_high_weighted(nums: list) -> str:
        x = 0
        num_breakpoint = len(nums)/2
        for num in nums:
            if int(num):  # taking advantage of the auto casting of int 1 and int 0 to bool
                x += 1
                if x > num_breakpoint:
                    return "high"
        if x == num_breakpoint:
            return "even"
        else:
            return "low"


    def reduce_numbers(numbers: list, index=0, focus_weighted=True) -> int:
        if len(numbers) == 1:
            return numbers[0]
        else:
            if focus_weighted and check_if_high_weighted([x[index] for x in numbers]) == "high":
                return reduce_numbers([x for x in numbers if x[index] == "1"], index=index + 1)
            elif focus_weighted and check_if_high_weighted([x[index] for x in numbers]) == "even":
                return reduce_numbers([x for x in numbers if x[index] == "1"], index=index + 1)
            elif focus_weighted and check_if_high_weighted([x[index] for x in numbers]) == "low":
                return reduce_numbers([x for x in numbers if x[index] == "0"], index=index + 1)
            elif not focus_weighted and check_if_high_weighted([x[index] for x in numbers]) == "high":
                return reduce_numbers([x for x in numbers if x[index] == "0"], index=index + 1, focus_weighted=False)
            elif not focus_weighted and check_if_high_weighted([x[index] for x in numbers]) == "even":
                return reduce_numbers([x for x in numbers if x[index] == "0"], index=index + 1, focus_weighted=False)
            elif not focus_weighted and check_if_high_weighted([x[index] for x in numbers]) == "low":
                return reduce_numbers([x for x in numbers if x[index] == "1"], index=index + 1, focus_weighted=False)


    print(
        f"The O2 generator rating is {reduce_numbers(numbers)}, the CO2 scrubber rating is {reduce_numbers(numbers, focus_weighted=False)}, thus the power rating is {int(reduce_numbers(numbers, focus_weighted=False), 2) * int(reduce_numbers(numbers), 2)}")

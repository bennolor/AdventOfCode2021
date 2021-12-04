import numpy as np

if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        numbers, *matrices = in_file.readlines()

    numbers = map(lambda x: int(x), numbers.split(','))
    matrices = np.loadtxt(matrices, int).reshape(-1, 5, 5)

    for number in numbers:
        # set called number
        matrices[matrices == number] = -42
        marked_numbers = (matrices == -42)
        win = (marked_numbers.all(1) | marked_numbers.all(2)).any(1)
        if win.any():
            result_score = (matrices * ~marked_numbers)[win].sum()
            break
    try:
        print(f"BINGO! The winning board has a score of {result_score} and the number that just got called was {number}. The answer is {result_score*number}")
    except NameError:
        print("Whoops something went wrong")

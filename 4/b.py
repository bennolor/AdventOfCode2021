import numpy as np

if __name__ == '__main__':
    with open('in.txt', 'r') as in_file:
        numbers, *matrices = in_file.readlines()

    numbers = map(lambda x: int(x), numbers.split(','))
    matrices = np.loadtxt(matrices, int).reshape(-1, 5, 5)

    wins = []
    for number in numbers:
        # set called number
        matrices[matrices == number] = -42
        marked_numbers = (matrices == -42)
        win = (marked_numbers.all(1) | marked_numbers.all(2)).any(1)
        if win.any():
            wins.append([(matrices * ~marked_numbers)[win].sum(), number])
            matrices = matrices[~win]

    try:
        print(f"BINGO! The last winning board has a score of {wins[-1][0]} and the number that just got called was {wins[-1][1]}. The answer is {wins[-1][0]*wins[-1][1]}")
    except NameError:
        pass

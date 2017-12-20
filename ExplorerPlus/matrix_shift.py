import guess
import random


def generate_shift_matrix(N):
    digits = generate_digits(N)
    row = digits
    # print(row)
    # print(left_shift(row))
    for i in range(N):
        print(row)
        row = left_shift(row)


def left_shift(row):
    result = []
    for i in range(1, len(row)):
        result.append(row[i])
    result.append(row[0])
    return result


def generate_digits(N):
    if N > 10:
        print("too many digits")
        return
    numbers = []
    n = random.randint(1, 9)
    numbers.append(n)
    for i in range(N):
        while n in numbers:
            n = random.randint(0, 9)
        numbers.append(n)
    return numbers

def main():
    generate_shift_matrix(5)

if __name__ == '__main__':
    main()
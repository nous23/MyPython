import random

def main():
    guess()



def generateFourDigit():
    numbers = []
    n = random.randint(1, 9)
    numbers.append(n)
    for i in range(3):
        while n in numbers:
            n = random.randint(0, 9)
        numbers.append(n)
    return numbers


def guess():
    digits = generateFourDigit()
    while True:
        user_digits = []
        user_number_str = input("Please input a four digits number: ")
        for s in user_number_str:
            digit = eval(s)
            user_digits.append(digit)
        result = ""
        for r in compare(user_digits, digits):
            result += r
        print(result)
        if result == "HHHH":
            break

def compare(userdigits, digits):
    result = []
    for i in range(4):
        if userdigits[i] < digits[i]:
            result.append("+")
        elif userdigits[i] > digits[i]:
            result.append("-")
        else:
            result.append("H")
    return result




if __name__ == "__main__":
    main()


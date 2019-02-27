import math
from cs50 import get_int


def digitCount(card):
    return len(str(card))


def checkSum(card):
    # checks card with Luhn's algorithm

    # reverse card
    card = str(card)
    card = int(''.join(reversed(card)))

    sum1 = 0
    sum2 = 0

    for i in range(1, digitCount(card), 2):  # gets every other digit starting at index 1, multiplies by two, adds sum of digits
        digit = int(str(card)[i]) * 2
        if digit >= 10:
            digit = int(str(digit)[0]) + int(str(digit)[1])
        sum1 = sum1 + digit

    for i in range(0, digitCount(card), 2):  # adds every other digit starting at index 0
        sum2 = sum2 + int(str(card)[i])

    sumCheck = (sum1 + sum2) % 10  # checks if the sum of the first and second sum ends in 0

    if sumCheck == 0:
        return True
    else:
        return False


def getFirstTwoDigits(card):
    # gets first two digits of card

    digit1 = int(str(card)[0]) * 10
    digit2 = int(str(card)[1])
    return digit1+digit2


def main():
    # checks card from user input

    card = get_int("What's your card number?\n")
    if checkSum(card):
        if (getFirstTwoDigits(card) == 34 or getFirstTwoDigits(card) == 37) and digitCount(card) == 15:
            print("AMEX\n")
        elif (getFirstTwoDigits(card) >= 40 and getFirstTwoDigits(card) <= 50) and (digitCount(card) == 13 or digitCount(card) == 16):
            print("VISA\n")
        elif (getFirstTwoDigits(card) >= 51 and getFirstTwoDigits(card) <= 55) and digitCount(card) == 16:
            print("MASTERCARD\n")
        else:
            print("INVALID\n")
    else:
        print("INVALID\n")


main()


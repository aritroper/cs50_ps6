import sys
from sys import argv
from cs50 import get_string


def caesar(text, rotations):
    newtext = ""
    for i in range(len(text)):
        if ord(text[i]) >= 65 and ord(text[i]) < 90:  # if it is a uppercase letter
            if ord(text[i]) + rotations >= 91:  # if surpasses letter dictionary, wrap around
                newtext += chr(((ord(text[i]) + rotations) % 91) + 65)
            else:
                newtext += chr(ord(text[i]) + rotations)
        elif ord(text[i]) >= 97 and ord(text[i]) < 122:  # if it is a lowercase letter
            if ord(text[i]) + rotations >= 123:  # if suprasses letter dictionary, wrap around
                newtext += chr(((ord(text[i]) + rotations) % 123) + 97)
            else:
                newtext += chr(ord(text[i]) + rotations)
        else:  # if it is not a letter
            newtext += text[i]
    return newtext


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit(1)

    str = get_string("plaintext: ")
    print("ciphertext: " + caesar(str, int(argv[1]) % 26))


main()


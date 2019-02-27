import sys
from cs50 import get_string
from sys import argv


def main():
    if len(sys.argv) != 2:   # checks arguments
        sys.exit(1)

    f = open(argv[1])
    list = []
    for line in f:
        line = line.rstrip('\n')  # strips new line
        list.append(line)
    str = get_string("What message would you like to censor?\n")
    words = str.split()
    for word in words:
        if word.lower() in list:  # censored word found!
            word = "*" * len(word)  # replace with * the length of the string
        print(word, end=" ")
    print("")


if __name__ == "__main__":
    main()

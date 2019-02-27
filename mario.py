from cs50 import get_int

# recursively prints # and spaces


def printLine(width, originalWidth):
    if width == 0:  # break if width == 0
        return
    else:
        for i in range(width-1):
            print(" ", end="")
        for i in range(originalWidth - width):
            print("#", end="")
        print("")
        printLine(width-1, originalWidth)


height = 0
#0 < height < 9
while height <= 0 or height >= 9:
    height = get_int("Height:\n")
printLine(height, height+1)
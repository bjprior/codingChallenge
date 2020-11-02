from number import Number

if __name__ == "__main__":
    # Open File
    file = open('testFile.txt', 'r')

    # Loop through lines
    for line in file:
        number = Number(line)
        number.print()

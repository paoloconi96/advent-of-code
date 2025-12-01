import pprint
from collections import defaultdict

def puzzle1():
    with open("input-1.txt") as inputFile:
        lines = [line.rstrip() for line in inputFile]
        result = 0
        position = 50
        for line in lines:
            if line[0] == "L":
                position -= int(line[1:])
            else:
                position += int(line[1:])

            while position < 0:
                position += 100

            while position > 99:
                position -= 100

            if position == 0:
                result += 1

        return result

def puzzle2():
    with open("input-2.txt") as inputFile:
        lines = [line.rstrip() for line in inputFile]
        result = 0
        position = 50
        for line in lines:
            was_zero = position == 0
            if line[0] == "L":
                position -= int(line[1:])
            else:
                position += int(line[1:])

            if position < 0 and not was_zero:
                result += 1

            result += int(abs(position / 100)) if position != 0 else 1
            position = position % 100

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())

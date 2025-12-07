import pprint
import re
from collections import defaultdict
from functools import reduce


def puzzle1():
    with (open("input-1.txt") as inputFile):
        grid = [list(line.rstrip()) for line in inputFile]
        operator_line = grid.pop()
        result = 0
        while grid[0]:
            while operator_line:
                operator = operator_line.pop()
                if operator != " " :
                    break

            line_value = 1 if operator == "*" else 0
            for line in grid:
                number = ""
                while line:
                    num = line.pop()
                    if num == " " and len(number) > 0:
                        break
                    if num == " ":
                        continue
                    number = num + number
                if operator == "*":
                    line_value *= int(number)
                else:
                    line_value += int(number)

            result += line_value

        return result

def puzzle2():
    with (open("input-1.txt") as inputFile):
        grid = [list(line) for line in inputFile]
        [line.pop() for line in grid]
        # Pycharm removes trailing spaces in lines
        grid[-1].append(" ")
        result = 0
        nums_operation = []
        while grid[-1]:
            number = []
            for line in grid:
                num = line.pop()
                if num != " ":
                    number.append(num)

            if len(number) == 0:
                continue

            operation = None
            if number[-1] == "*" or number[-1] == "+":
                operation = number.pop()

            nums_operation.append(int("".join(number)))
            if operation == "*":
                result += reduce(lambda x,y: x*y, nums_operation, 1)
                nums_operation = []
            elif operation == "+":
                result += sum(nums_operation)
                nums_operation = []

        return result

if __name__ == '__main__':
    print("Puzzle 1: {}".format(puzzle1()))
    print("Puzzle 2: {}".format(puzzle2()))

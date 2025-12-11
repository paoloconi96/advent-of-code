import pprint
import re
from collections import defaultdict
from functools import reduce

def puzzle1():
    with (open("input-1.txt") as inputFile):
        grid = [line.rstrip() for line in inputFile]
        serverMap = {}
        for line in grid:
            key, links = line.split(": ")
            serverMap[key] = links.split(" ")

        visited = set()
        return solve(serverMap, "you", visited)

def solve(serverMap, el, visited):
    if el == "out":
        return 1

    if isinstance(serverMap[el], int):
        return serverMap[el]

    if el in visited:
        print("Surpise MF")
        return 0

    visited.add(el)

    paths = 0
    for child in serverMap[el]:
        paths += solve(serverMap, child, visited)

    serverMap[el] = paths
    return serverMap[el]

def puzzle2():
    with (open("input-1.txt") as inputFile):
        grid = [list(line.rstrip()) for line in inputFile]
        pass

if __name__ == '__main__':
    print("Puzzle 1: {}".format(puzzle1()))
    # print("Puzzle 2: {}".format(puzzle2()))

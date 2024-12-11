import math
from collections import defaultdict


def puzzle(iterations):
    with open("input-1.txt") as inputFile:
        stones = defaultdict(int)
        for n in inputFile.read().rstrip().split(" "):
            stones[int(n)] += 1

    for _ in range(iterations):
        newStones = defaultdict(int)
        for stone, amount in stones.items():
            stoneDigits = int(math.log10(stone))+1 if stone != 0 else 1
            if stone == 0:
                newStones[1] += amount
            elif stoneDigits % 2 == 0:
                divisor = 10 ** (stoneDigits // 2)
                newStones[stone // divisor] += amount
                newStones[stone % divisor] += amount
            else:
                newStones[stone * 2024] += amount

        stones = newStones

    return sum(stones.values())

if __name__ == '__main__':
    print("Result from puzzle 1 is: {}".format(puzzle(25)))
    print("Result from puzzle 2 is: {}".format(puzzle(75)))

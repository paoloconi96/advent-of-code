import bisect
import collections
import pprint
from collections import defaultdict

def puzzle1():
    with (open("input-1a.txt") as inputFile):
        lines = collections.deque([line.rstrip() for line in inputFile])

        jump_list = []
        while lines:
            line = lines.popleft()
            if line == "":
                break
            start, end = line.split("-")

            jump_list.append((int(start), int(end)))

        jump_list.sort()

        result = 0
        while lines:
            product = int(lines.popleft())
            # Could be a binary search for faster search
            for start, end in jump_list:
                if product < start:
                    break
                if end < product:
                    continue

                result += 1
                break

        return result

def puzzle2():
    with (open("input-1a.txt") as inputFile):
        lines = collections.deque([line.rstrip() for line in inputFile])

        jump_list = []
        while lines:
            line = lines.popleft()
            if line == "":
                break
            start, end = line.split("-")

            jump_list.append((int(start), int(end)))

        jump_list.sort()
        jump_list = collections.deque(jump_list)

        result_list = [jump_list[0]]
        while jump_list:
            start, end = jump_list.popleft()
            prev_start, prev_end = result_list[-1]
            new_start, new_end = None, None
            if end <= prev_start or start <= prev_end:
                new_start = min(prev_start, start)
                new_end = max(prev_end, end)

            if new_start is not None:
                result_list[-1] = (new_start, new_end)
            else:
                result_list.append((start, end))

        result = 0
        for start, end in result_list:
            result += end - start + 1

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())

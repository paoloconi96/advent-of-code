from math import log

def compute_sum_multiply(total, subtotal, comps, i):
    if i == len(comps):
        return total if total == subtotal else 0

    return max(
        compute_sum_multiply(total, subtotal + comps[i], comps, i + 1),
        compute_sum_multiply(total, subtotal * comps[i], comps, i + 1),
    )

def puzzle1():
    with open("input-1.txt") as inputFile:
        result = 0
        for line in inputFile:
            total, comps = line.rstrip().split(": ")
            total, comps = int(total), [int(n) for n in comps.split(" ")]
            result+= compute_sum_multiply(total, comps[0], comps, 1)

        return result

def compute_sum_multiply_concat(total, subtotal, comps):
    if len(comps) == 0:
        return total if total == subtotal else 0

    return max(
        compute_sum_multiply_concat(total, subtotal + comps[0], comps[1:]),
        compute_sum_multiply_concat(total, subtotal * comps[0], comps[1:]),
        compute_sum_multiply_concat(total, 10 ** int(log(comps[0], 10) + 1) * subtotal + comps[0], comps[1:]),
    )

def puzzle2():
    with open("input-1.txt") as inputFile:
        result = 0
        for line in inputFile:
            total, comps = line.rstrip().split(": ")
            total, comps = int(total), [int(n) for n in comps.split(" ")]
            result+= compute_sum_multiply_concat(total, comps[0], comps[1:])

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())

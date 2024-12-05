from collections import defaultdict

def check_pages(pages, dependencies):
    visited = set()
    pages_set = set(pages)
    for page in pages:
        for dep in dependencies[page]:
            if dep in pages_set and dep not in visited:
                return 0

        visited.add(page)

    return int(pages[len(pages) // 2])

def puzzle1():
    with open("input-1.txt") as inputFile:
        dependencies = defaultdict(list)
        for line in inputFile:
            if line == "\n":
                break

            depend, val = line.rstrip().split("|")
            dependencies[val].append(depend)

        result = 0
        for line in inputFile:
            pages = line.rstrip().split(",")
            result += check_pages(pages, dependencies)

        return result

def fix_error(pages, dependencies, with_error):
    visited = set()
    pages_set = set(pages)
    for i in range(len(pages)):
        page = pages[i]
        for dep in dependencies[page]:
            if dep in pages_set and dep not in visited:
                pages.remove(dep)
                pages.insert(i, dep)
                return fix_error(pages, dependencies, True)

        visited.add(page)

    return int(pages[len(pages) // 2]) if with_error else 0

def puzzle2():
    with open("input-1.txt") as inputFile:
        dependencies = defaultdict(list)
        for line in inputFile:
            if line == "\n":
                break

            depend, val = line.rstrip().split("|")
            dependencies[val].append(depend)

        result = 0
        for line in inputFile:
            pages = line.rstrip().split(",")
            result += fix_error(pages, dependencies, False)

        return result

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())

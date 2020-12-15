import re
from collections import defaultdict

def import_lines(filepath):

    bags = defaultdict(dict)

    with open(filepath) as f:
        lines = f.read().splitlines()

    for l in lines:
        bag = re.match(r'(.*) bags contain', l).groups()[0]
        for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
            bags[bag][b] = int(count)

    return(bags)


def part1(bags, colour = "shiny gold"):
    answer = set()

    def search(colour):
        for b in bags:
            if colour in bags[b]:
                answer.add(b)
                search(b)
    search(colour)
    return len(answer)


def part2(bags):
    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = bags[bag][s]
            count += multiplier * search(s)
        return count
    return search('shiny gold') - 1  # Rm one for shiny gold itself


if __name__ == "__main__":
    bags = import_lines("./day7_input.txt")
    print("Part1: ", part1(bags))
    print("Part2: ", part2(bags))

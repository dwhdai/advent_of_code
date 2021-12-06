from collections import Counter
from dataclasses import dataclass, replace
from itertools import product
from typing import List, Tuple

with open("day5_input.txt", "r") as f:
    content = f.readlines()
    lines = [l.split(" -> ") for l in content]
    raw_coordinates = [tuple([int(x) for x in p.strip().split(',')]) for l in lines for p in l]
    line_coordinates = [raw_coordinates[i:i+2] for i in range(0, len(raw_coordinates), 2)]

@dataclass
class Line:
    start: Tuple[int, int]
    end: Tuple[int, int]

    def order_points(self):
        # Check if x/ys are backwards
        xstart, xend = self.start[0], self.end[0]
        ystart, yend = self.start[1], self.end[1]
        start = tuple([xend, yend])
        end = tuple([xstart, ystart])
        return replace(self, start=start, end=end)

    def get_points(self) -> List[Tuple[int, int]]:
        if self.start[0] > self.end[0] or self.start[1] > self.end[1]:
            self = self.order_points()
        x_s = list(range(self.start[0], self.end[0]+1, 1))
        y_s = list(range(self.start[1], self.end[1]+1, 1))
        points = list(product(x_s, y_s))
        return points

    def straight(self) -> bool:
        if self.start[0] == self.end[0] or self.start[1] == self.end[1]:
            return True
        return False

@dataclass
class Lines:
    line: List[Line]

def part1(line_coordinates):
    points = []
    lines = [Line(line[0], line[1]) for _, line in enumerate(line_coordinates)]
    for line in lines:
        if line.straight():
            points.extend(line.get_points())
    points_counts = Counter(points)
    two_or_more = [x for x in points_counts.values() if x >= 2]
    return len(two_or_more)

if __name__ == "__main__":
    print(part1(line_coordinates))

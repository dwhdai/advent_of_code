from typing import List

def count_depth_increases(depth_readings: List[int]):
    increased = [1 for i, d in enumerate(depth_readings) if d > depth_readings[i-1]]
    return sum(increased)

def count_depth_increases_sliding_window(depth_readings: List[int]):
    increased = [1 for i, d in enumerate(depth_readings) if d > depth_readings[i-3]]
    return sum(increased)

def main(depth_readings: List[int]):
    part1 = count_depth_increases(depth_readings)
    part2 = count_depth_increases_sliding_window(depth_readings)
    print(part1, part2)

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        input = [int(line.strip()) for line in f]
    main(input)

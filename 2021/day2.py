
with open("day2_input.txt", "r") as f:
    instructions = [(l.split()[0], int(l.split()[1])) for l in f]

# Change up steps to negative
instructions = [(dir, -steps) if dir == "up" else (dir, steps) for (dir, steps) in instructions]

def part1(instructions):
    horizontal = [steps for (dir, steps) in instructions if dir=="forward"]
    vertical = [steps for (dir, steps) in instructions if dir in ["up", "down"]]
    answer = sum(horizontal) * sum(vertical)
    return answer


def part2(instructions):

    horizontal = [steps for (dir, steps) in instructions if dir=="forward"]
    aim = []
    for i, (dir, a) in enumerate(instructions):
        if i == 0 and dir in ["up", "down"]:
            aim.append(a)
        elif i == 0 and dir == "forward":
            aim.append(0)
        elif dir in ["forward"]:
            aim.append(aim[i-1])
        else:
            a = a + aim[i-1]
            aim.append(a)

    vertical = [aim*steps for (aim, (dir, steps)) in zip(aim, instructions) if dir=="forward"]
    answer = sum(horizontal) * sum(vertical)
    return answer

print(part1(instructions))
print(part2(instructions))



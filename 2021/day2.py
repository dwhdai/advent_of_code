
with open("2021/day2_input.txt", "r") as f:
    instructions = [(l.split()[0], int(l.split()[1])) for l in f]

# Change up steps to negative
instructions = [(dir, -steps) if dir == "up" else (dir, steps) for (dir, steps) in instructions]
horizontal = [steps for (dir, steps) in instructions if dir=="forward"]
vertical = [steps for (dir, steps) in instructions if dir in ["up", "down"]]
answer = sum(horizontal) * sum(vertical)
print(answer)

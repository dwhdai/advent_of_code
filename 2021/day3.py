# test = ["00100",
#         "11110",
#         "10110",
#         "10111",
#         "10101",
#         "01111",
#         "00111",
#         "11100",
#         "10000",
#         "11001",
#         "00010",
#         "01010"]

with open("day3_input.txt", "r") as f:
    diagnostics = [line.strip() for line in f]

def get_gamma(diagnostics):
    gamma = ''
    for i in range(len(diagnostics[0])):
        zeros = 0
        ones = 0
        for _, line in enumerate(diagnostics):
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma = gamma + '0'
        else: 
            gamma = gamma + '1'
    return gamma

def get_episilon(gamma):
    epsilon = [1 if g=="0" else 0 for g in gamma]
    return ''.join(str(e) for e in epsilon)

def part1(diagnostics):
    gamma = get_gamma(diagnostics)
    epsilon = get_episilon(gamma)
    return int(gamma, 2) * int(epsilon, 2)

print(part1(diagnostics))



def get_oxygen(diagnostics):
    
    for i in range(len(diagnostics[0])):
        if len(diagnostics) == 1:
            return diagnostics[0]
        zeros = 0
        ones = 0
        for line in diagnostics:
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            diagnostics = [d for d in diagnostics if d[i]=="0"]
        else:
            diagnostics = [d for d in diagnostics if d[i]=="1"]

    return diagnostics[0]

def get_co2(diagnostics):

    for i in range(len(diagnostics[0])):
        if len(diagnostics) == 1:
            return diagnostics[0]
        zeros = 0
        ones = 0
        for line in diagnostics:
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            diagnostics = [d for d in diagnostics if d[i]=="1"]
        else:
            diagnostics = [d for d in diagnostics if d[i]=="0"]

    return diagnostics[0]

def part2(diagnostics):
    oxygen = get_oxygen(diagnostics)
    co2 = get_co2(diagnostics)
    return int(oxygen, 2) * int(co2, 2)
print(part2(diagnostics))

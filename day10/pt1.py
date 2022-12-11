def main():
    with open('input1.txt') as f:
        strengthSignals = findStrengthSignals(f)
        print(strengthSignals)
        print(sum(strengthSignals.values()))

    f.closed

def findStrengthSignals(f):
    strengthSignals = {}
    cycle = 0
    x = 1
    
    for line in f:
        instruction = line.split()
        if instruction[0] == 'addx':
            cycle += 1
            checkSignalStrength(cycle, x, strengthSignals)
            cycle += 1
            checkSignalStrength(cycle, x, strengthSignals)
            x += int(instruction[1])
        elif instruction[0] == 'noop':
            cycle += 1
            checkSignalStrength(cycle, x, strengthSignals)
    return strengthSignals
        

def checkSignalStrength(cycle, x, strengthSignals):
    checklist = [20, 60, 100, 140, 180, 220]

    if cycle == 220:
        print(x)

    if cycle in checklist:
        strengthSignals[cycle] = cycle * x

main()
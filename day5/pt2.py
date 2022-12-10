import re

def main():
    with open('input1.txt') as f:
        stacksAndCrates = readCrates(f)
        instructions = readInstructions(f)
        moveCrates(stacksAndCrates, instructions)
        prettyPrintStacksAndCrates(stacksAndCrates)
        print(getTopCrates(stacksAndCrates))

    f.closed

def readCrates(f):
    stacksAndCrates = []

    for line in f:
        if re.match('( \d+ )+', line):
            break

        if len(stacksAndCrates) <= 0:
            stacksAndCrates = [[] for i in range(0, len(line), 4)]
            numOfStacks = len(stacksAndCrates)

        nextCratesRow = [line[i:i+4].strip() for i in range(0, len(line), 4)]

        for i in range(numOfStacks):
            if nextCratesRow[i] != '':
                stacksAndCrates[i].insert(0,nextCratesRow[i])

    return stacksAndCrates

def readInstructions(f):
    instructions = []

    f.readline()
    for line in f:
        match = re.match('move (\d+) from (\d+) to (\d+)', line)
        t = tuple(match.group(i) for i in range(1, 4))
        instructions.append(t)

    return instructions

def moveCrates(stacksAndCrates, instructions):
    for instruction in instructions:
        numOfCrates = int(instruction[0])*-1
        fromStack = int(instruction[1])-1
        toStack = int(instruction[2])-1

        poppedStack = stacksAndCrates[fromStack][numOfCrates:]
        stacksAndCrates[toStack].extend(poppedStack)
        stacksAndCrates[fromStack] = stacksAndCrates[fromStack][:numOfCrates]

        # prettyPrintStacksAndCrates(stacksAndCrates)
        
    return stacksAndCrates

def prettyPrintStacksAndCrates(stacksAndCrates):
    print('**********')
    for stack in stacksAndCrates:
        print(stack)
    print('**********')

def getTopCrates(stacksAndCrates):
    topCrates = ''
    for stack in stacksAndCrates:
        if len(stack) > 0:
            topCrates += stack.pop()[1]

    return topCrates

main() 
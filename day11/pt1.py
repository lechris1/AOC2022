from monkey import Monkey

def main():
    with open('input1.txt') as f:
        monkeyList = readMonkeys(f)
        throwShitAround(monkeyList)

    f.closed

def readMonkeys(f):
    monkeyList = []
    for line in f:
        monkeyList.append(createMonkey(line.split()[1][0], f))

    return monkeyList

def createMonkey(monkeyId, f):
    lineNum = 0
    items = []
    operation = []
    test = 0
    trueTest = 0
    falseTest = 0

    for line in f:
        match lineNum:
            case 0:
                items = line[18:].strip().split(', ')
            case 1:
                operation = line[23:].split()
            case 2:
                test = int(line[21:])
            case 3:
                trueTest = int(line[29:])
            case 4:
                falseTest = int(line[30:])
            case other:
                return Monkey(monkeyId, [int(item) for item in items], operation, (test, trueTest, falseTest))

        lineNum += 1

def throwShitAround(monkeyList):
    stop = 0
    while stop < 20:
        for monkey in monkeyList:
            monkey.inspectItems()
            thrownItems = monkey.throwItems()

            # print(monkeyList)

            for item in thrownItems:
                monkeyList[item[0]].catchItem(item[1])

        print('Round: ' + str(stop))
        print(monkeyList)

        stop += 1

main()
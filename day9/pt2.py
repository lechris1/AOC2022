NUM_OF_NODES = 10

def main():
    with open('input1.txt') as f:
        instructions = readInstructions(f)
        visitedMap = traverse(instructions)
        print(countVisited(visitedMap))

    f.closed

def readInstructions(f):
    instructions = []
    for line in f:
        instructions.append(line.split())

    return instructions

# Note: cannot use same approach as pt1 because non-head nodes can move diagonally
def traverse(instructions):
    visitedMap = {}
    fullRope = [[0,0] for i in range(NUM_OF_NODES)]

    for instruction in instructions:
        # print(instruction)
        for i in range(1, int(instruction[1])+1):
            headPrev = [*fullRope[0]]
            match instruction[0]:
                case 'U':
                    fullRope[0][0] += 1
                case 'D':
                    fullRope[0][0] -= 1
                case 'R':
                    fullRope[0][1] += 1
                case 'L':
                    fullRope[0][1] -= 1
            
            for j in range(1, NUM_OF_NODES):
                moveNextNode(fullRope, j, visitedMap)
                # print(fullRope)
            # printFullRope(fullRope)

    return visitedMap

def moveNextNode(fullRope, nodeNum, visitedMap):
    headTailX = fullRope[nodeNum-1][0] - fullRope[nodeNum][0]
    headTailY = fullRope[nodeNum-1][1] - fullRope[nodeNum][1]

    if abs(headTailX) > 1 or abs(headTailY) > 1:
        xMove = calculateXMove(headTailX, headTailY)
        yMove = calculateYMove(headTailY, headTailX)
        # print('************')
        # print(fullRope)
        # print(nodeNum)
        # print(nodePrev)
        # print('************')
        fullRope[nodeNum] = [fullRope[nodeNum][0]+xMove, fullRope[nodeNum][1]+yMove]
        if nodeNum+1 == NUM_OF_NODES:
            visitedMap[tuple(fullRope[nodeNum])] = True
            # print(fullRope)
            # countVisited(visitedMap)

    return None

def calculateXMove(headTailX, headTailY):
    xMove = 0
    if headTailX > 1 or (headTailX == 1 and abs(headTailY) > 1):
        xMove = 1
    elif headTailX < -1 or (headTailX == -1 and abs(headTailY) > 1):
        xMove = -1

    return xMove

def calculateYMove(headTailY, headTailX):
    yMove = 0
    if headTailY > 1 or (headTailY == 1 and abs(headTailX) > 1):
        yMove = 1
    elif headTailY < -1 or (headTailY == -1 and abs(headTailX) > 1):
        yMove = -1

    return yMove

def countVisited(visitedMap):
    # visualMap = [['.' for j in range(40)] for i in range(40)]
    # print(visitedMap)
    visitedMap[(0,0)] = '#'
    count = 0
    for key, value in visitedMap.items():
        if value:
            # visualMap[key[0]+15][key[1]+15] = '#'
            count += 1

    # printMap(visualMap)
    return count

def printMap(map):
    map.reverse()
    for row in map:
        print(''.join(row))

def printFullRope(fullRope):
    visualMap = [['.' for j in range(10)] for i in range(10)]
    for i in range(len(fullRope)):
        visualMap[fullRope[i][0]][fullRope[i][1]] = str(i)

    printMap(visualMap)

main()
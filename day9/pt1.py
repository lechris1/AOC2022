def main():
    with open('input11.txt') as f:
        instructions = readInstructions(f)
        visitedMap = traverse(instructions)
        print(countVisited(visitedMap))

    f.closed

def readInstructions(f):
    instructions = []
    for line in f:
        instructions.append(line.split())

    return instructions

# Note: using head's previous location worked instead of manually calculating tail's next spot
# becuase head only moved in cardinal directions
def traverse(instructions):
    visitedMap = {}
    head = [0,0]
    tail = [0,0]

    for instruction in instructions:
        for i in range(1, int(instruction[1])+1):
            headPrev = [*head] 
            match instruction[0]:
                case 'U':
                    head[0] += 1
                case 'D':
                    head[0] -= 1
                case 'R':
                    head[1] += 1
                case 'L':
                    head[1] -= 1
            
            # print([head, tail])
            headTailX = head[0] - tail[0]
            headTailY = head[1] - tail[1]
            # print(headTailX)
            # print(headTailY)
            if abs(headTailX) > 1 or abs(headTailY) > 1:
                tail = headPrev
                visitedMap[tuple(tail)] = True

                # print('head:')
                # print(head)
                # print('tail:')
                # print(tail)
                # print('************')

        # print('head:')
        # print(head)

    return visitedMap

def countVisited(visitedMap):
    # visualMap = [['.' for j in range(10)] for i in range(10)]
    # print(visitedMap)
    visitedMap[(0,0)] = '#'
    count = 0
    for key, value in visitedMap.items():
        if value:
            # visualMap[key[0]][key[1]] = '#'
            count += 1

    # printMap(visualMap)
    return count

def printMap(map):
    map.reverse()
    for row in map:
        print(''.join(row))

main()
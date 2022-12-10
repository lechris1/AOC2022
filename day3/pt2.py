def main():
    with open('input1.txt') as f:
        sharedItems = findSharedItem(f)
        print(calculatePriority(sharedItems)) #pt1

    f.closed

def findSharedItem(f):
    sharedItems = []
    groupRucksacks = []
    for line in f:
        if len(groupRucksacks) < 3:
            groupRucksacks.append(sorted([*line.strip()]))

        if len(groupRucksacks) == 3:
            sharedItem = None
            i = 0
            j = 0
            k = 0
            while sharedItem == None:
                if groupRucksacks[0][i] == groupRucksacks[1][j] and groupRucksacks[0][i] == groupRucksacks[2][k]:
                    sharedItem = groupRucksacks[0][i]
                else:
                    incrementResult = checkIndexIncrement(groupRucksacks, i, j, k)
                    if 'i' in incrementResult:
                        i = incrementResult['i']
                    elif 'j' in incrementResult:
                        j = incrementResult['j']
                    elif 'k' in incrementResult:
                        k = incrementResult['k']
            
            sharedItems.append(sharedItem)

            #reset list after finding shared item
            groupRucksacks = []
        
    return sharedItems

def calculatePriority(sharedItems):
    priorityScore = 0
    for i in range(len(sharedItems)):
        if sharedItems[i].isupper():
            priorityScore += ord(sharedItems[i]) - ord('A') + 27
        else:
            priorityScore += ord(sharedItems[i]) - ord('a') + 1
        

    return priorityScore

def checkIndexIncrement(groupRucksacks, i, j, k):
    result = {}

    if groupRucksacks[0][i] < groupRucksacks[1][j] or groupRucksacks[0][i] < groupRucksacks[2][k]:
        i += 1
        result['i'] = i
    elif groupRucksacks[1][j] < groupRucksacks[0][i] or groupRucksacks[1][j] < groupRucksacks[2][k]:
        j += 1
        result['j'] = j
    elif groupRucksacks[2][k] < groupRucksacks[0][i] or groupRucksacks[2][k] < groupRucksacks[1][j]:
        k += 1
        result['k'] = k

    return result

main()
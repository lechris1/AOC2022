def main():
    with open('input1.txt') as f:
        sharedItems = findSharedItem(f)
        print(calculatePriority(sharedItems)) #pt1

    f.closed

def findSharedItem(f):
    sharedItems = []
    for line in f:
        itemList = [*line.strip()]
        halfwayIndex = int(len(itemList)/2)
        compartment1 = sorted(itemList[0:halfwayIndex])
        compartment2 = sorted(itemList[halfwayIndex:len(line.strip())])
        sharedItem = None

        i = 0
        j = 0
        while sharedItem == None:
            if compartment1[i] == compartment2[j]:
                sharedItem = compartment1[i]
            else:
                if compartment1[i] > compartment2[j]:
                    j += 1
                else:
                    i += 1
        
        sharedItems.append(sharedItem)

        
    return sharedItems

def calculatePriority(sharedItems):
    priorityScore = 0
    for i in range(len(sharedItems)):
        if sharedItems[i].isupper():
            priorityScore += ord(sharedItems[i]) - ord('A') + 27
        else:
            priorityScore += ord(sharedItems[i]) - ord('a') + 1
        

    return priorityScore

main()
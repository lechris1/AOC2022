def main():
    with open('input1.txt') as f:
        rationsList = getRations(f)
        print(rationsList[0]) #pt1
        print(sum(rationsList[0:3])) #pt2

    f.closed

def getRations(f):
    rationList = []
    currentRation = 0
    for line in f:
        ration = line.strip()
        if ration == '':
            rationList.append(currentRation)
            currentRation = 0
        else:
            currentRation += int(ration)
        
    rationList.sort(reverse=True)
    return rationList

main()
def main():
    with open('input1.txt') as f:
        trees = readTrees(f)
        print(countVisibleTrees(trees))

    f.closed

def readTrees(f):
    trees = []
    for line in f:
        trees.append([ch for ch in line.strip()])

    return trees

def prettyPrint(trees):
    for stack in trees:
        print(stack)

def countVisibleTrees(trees):
    count = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if i == 0 or j == 0 or i == len(trees)-1 or j == len(trees[i])-1:
                count += 1
            elif (checkNorthVisible(i, j, trees)
                or checkEastVisible(i, j, trees) 
                or checkWestVisible(i, j, trees) 
                or checkSouthVisible(i, j, trees)):
                # print(str(i) + ' ' + str(j))
                count += 1
            

    return count

def checkNorthVisible(i, j, trees):
    isVisible = True
    nextIndex = i-1
    while nextIndex >= 0:
        if trees[nextIndex][j] >= trees[i][j]:
            isVisible = False
        nextIndex -= 1

    return isVisible

def checkEastVisible(i, j, trees):
    # print('start: ' + str(i) + ',' + str(j))
    isVisible = True
    nextIndex = j+1
    while nextIndex < len(trees[i]):
        # print(str(trees[nextIndex][j]) + ',' + str(trees[i][j]))
        if trees[i][nextIndex] >= trees[i][j]:
            isVisible = False
        nextIndex += 1

    return isVisible

def checkWestVisible(i, j, trees):
    isVisible = True
    nextIndex = j-1
    while nextIndex >= 0:
        if trees[i][nextIndex] >= trees[i][j]:
            isVisible = False
        nextIndex -= 1

    return isVisible

def checkSouthVisible(i, j, trees):
    isVisible = True
    nextIndex = i+1
    while nextIndex < len(trees):
        if trees[nextIndex][j] >= trees[i][j]:
            isVisible = False
        nextIndex += 1

    return isVisible

main()
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
    highestScenicScore = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            scenicScore = (checkNorthVisible(i, j, trees)
                * checkEastVisible(i, j, trees) 
                * checkWestVisible(i, j, trees) 
                * checkSouthVisible(i, j, trees))

            if scenicScore > highestScenicScore:
                # print('start: ' + str(i) + ',' + str(j))
                highestScenicScore = scenicScore
                # print(highestScenicScore)
            

    return highestScenicScore

def checkNorthVisible(i, j, trees):
    count = 0
    isVisible = True
    nextIndex = i-1
    while nextIndex >= 0:
        if trees[nextIndex][j] < trees[i][j]:
            count += 1
        else:
            count += 1
            break
        nextIndex -= 1

    return count

def checkEastVisible(i, j, trees):
    count = 0
    # print('start: ' + str(i) + ',' + str(j))
    isVisible = True
    nextIndex = j+1
    while nextIndex < len(trees[i]):
        # print(str(trees[nextIndex][j]) + ',' + str(trees[i][j]))
        if trees[i][nextIndex] < trees[i][j]:
            count += 1
        else:
            count += 1
            break
        nextIndex += 1

    return count

def checkWestVisible(i, j, trees):
    count = 0
    isVisible = True
    nextIndex = j-1
    while nextIndex >= 0:
        if trees[i][nextIndex] < trees[i][j]:
            count += 1
        else:
            count += 1
            break
        nextIndex -= 1

    return count

def checkSouthVisible(i, j, trees):
    count = 0
    isVisible = True
    nextIndex = i+1
    while nextIndex < len(trees):
        if trees[nextIndex][j] < trees[i][j]:
            count += 1
        else:
            count += 1
            break
        nextIndex += 1

    return count

main()
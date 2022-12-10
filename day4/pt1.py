def main():
    with open('input1.txt') as f:
        completeOverlaps = findCompleteOverlaps(f)
        print(completeOverlaps) #pt1

    f.closed

def findCompleteOverlaps(f):
    completeOverlaps = 0
    for line in f:
        pairs = line.strip().split(',')
        completeOverlaps += checkCompleteOverlap(pairs[0].split('-'), pairs[1].split('-'))

    return completeOverlaps

def checkCompleteOverlap(pair1, pair2):
    isCompleteOverlap = 0
    if (
            (int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1]))
            or (int(pair2[0]) <= int(pair1[0]) and int(pair2[1]) >= int(pair1[1]))
        ):
        isCompleteOverlap = 1

    return isCompleteOverlap


main()
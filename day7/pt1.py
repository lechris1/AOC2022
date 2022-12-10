from fileTree import FileTree
from directory import Directory
from file import File

def main():
    with open('input1.txt') as f:
        fileTree = readCommands(f)
        # print(fileTree)
        # print(fileTree.__sizeof__())
        # print(fileTree.findDirsOfSize(100000))
        print(fileTree.clearUpSpace(30000000 - (70000000 - fileTree.__sizeof__())))

    f.closed

def readCommands(f):
    fileTree = None
    for line in f:
        list = line.split()
        if list[0] == '$' and list[1] == 'cd':
            fileTree = processCd(list, fileTree)
        elif list[0] == '$' and list[1] == 'ls':
            nextCommand = fileTree.ls(f)
            if nextCommand != None:
                processCd(nextCommand, fileTree)

    return fileTree

def processCd(list, fileTree):
    if list[2] == '..':
        fileTree.cd('..')
    elif list[2] == '/':
        fileTree = FileTree(Directory('/', None))
    else:
        fileTree.cd(list[2])

    return fileTree

main()
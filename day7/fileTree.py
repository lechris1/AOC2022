from directory import Directory

class FileTree:
    def __init__(self, rootDir):
        self.root = rootDir
        self.currentDir = rootDir

    def cd(self, name):
        self.currentDir = self.currentDir.cd(name)
        # print(self.currentDir)

    def ls(self, file):
        for line in file:
            list = line.split()
            # print(line)
            if list[0] == '$' and list[1] == 'cd':
                return list
            elif list[0] == 'dir':
                self.currentDir.addDir(list[1])
            else:
                self.currentDir.addFile(*list)
    
    def findDirsOfSize(self, size):
        return self.root.findDirsOfSize(size)

    def clearUpSpace(self, minSize):
        return self.root.clearUpSpace(minSize)

    def __repr__(self):
        return self.root.__str__()

    def __sizeof__(self):
        return self.root.__sizeof__()

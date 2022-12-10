from file import File

class Directory:
    def __init__(self, name, parentDir):
        self.name = name
        self.parentDir = parentDir
        self.items = []
        self.files = []

    def cd(self, name):
        try:
            index = self.items.index(name)
        except ValueError:
            index = None
        
        if index != None:
            return self.items[index]
        elif name == '..':
            return self.parentDir

    def addDir(self, name):
        self.items.append(Directory(name, self))

    def addFile(self, size, name):
        self.items.append(File(name, size))

    #pt1
    def findDirsOfSize(self, size):
        sum = 0
        for item in self.items:
            if isinstance(item, Directory):
                itemSize = item.__sizeof__()
                if itemSize <= size:
                    sum += itemSize
                sum += item.findDirsOfSize(size)

        return sum

    #pt2
    def clearUpSpace(self, minSize):
        deletedDir = ''
        deletedDirSize = 0
        dirSize = self.__sizeof__()
        # print('entering dir: ' + self.name)
        # print('dir size: ' + str(dirSize))

        if dirSize >= minSize:
            deletedDir = self.name
            deletedDirSize = dirSize

            for item in self.items:
                # print('***********')
                # print(self.name)
                # print(item.__sizeof__())
                if isinstance(item, Directory):
                    possibleDir = item.clearUpSpace(minSize)
                    if possibleDir[0] != '' and possibleDir[1] < deletedDirSize:
                        deletedDir = possibleDir[0]
                        deletedDirSize = possibleDir[1]

        # print(deletedDir, deletedDirSize)
        return (deletedDir, deletedDirSize)

    def __repr__(self):
        return self.name + ': ' + self.items.__str__()

    def __eq__(self, other):
        return self.name == other

    def __sizeof__(self):
        sum = 0
        for item in self.items:
            sum += int(item.__sizeof__())

        return sum

    # def __iter__(self):
    #     return self.items.__iter__()
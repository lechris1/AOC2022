class Monkey:
    def __init__(self, id, items, operation, throwInstruction):
        self.id = id
        self.items = items
        self.operation = operation
        self.throwInstruction = throwInstruction
        self.inspectCount = 0

    def throwItems(self):
        receivingMonkeys = []
        for item in self.items:
            if item % self.throwInstruction[0] == 0:
                receivingMonkeys.append((self.throwInstruction[1], item))
            else:
                receivingMonkeys.append((self.throwInstruction[2], item))

        self.items = []
        return receivingMonkeys

    def inspectItems(self, lcm = 3):
        # if len(self.items) > 0:
        #     print(self.items[0])
        thrownItems = []
        for item in self.items:
            thrownItem = item

            modifier = 0
            if self.operation[1] == 'old':
                modifier = item
            else:
                modifier = int(self.operation[1])

            match self.operation[0]:
                case '+':
                    thrownItem += modifier
                case '-':
                    thrownItem -= modifier
                case '*':
                    thrownItem *= modifier
                case '/':
                    thrownItem //= modifier

            # thrownItem //= 3 #pt1
            thrownItem %= lcm #pt2
            thrownItems.append(thrownItem)
            self.inspectCount += 1

        # print(thrownItems)
        self.items = thrownItems

    def catchItem(self, item):
        self.items.append(item)

    def __repr__(self):
        # return self.id + ': ' + self.items.__str__()
        return self.id + ': ' + str(self.inspectCount)
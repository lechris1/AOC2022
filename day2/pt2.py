from enum import Enum

class Weapon(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Outcome(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

class Round():
    def __init__(self, weaponList):
        self.p1Weapon = Weapon(ord(weaponList[0].strip()) - ord('A'))
        self.outcome = Outcome((ord(weaponList[1].strip()) - ord('X')) * 3)
        self.p2Weapon = None
    
    def calculateMyWeapon(self):
        match self.outcome.value/3:
            case 0:
                self.p2Weapon = Weapon((self.p1Weapon.value - 1) % 3)
            case 1:
                self.p2Weapon = Weapon(self.p1Weapon.value)
            case 2:
                self.p2Weapon = Weapon((self.p1Weapon.value + 1) % 3)

    def play(self):
        if (self.p1Weapon.value - self.p2Weapon.value)%3 == 1:
            return Outcome.LOSE
        elif self.p1Weapon.value == self.p2Weapon.value:
            return Outcome.DRAW
        else:
            return Outcome.WIN

def main():
    with open('input1.txt') as f:
        score = getScore(f)
        print(score) #pt1

    f.closed

def getScore(f):
    score = 0
    for line in f:
        round = Round(line.split(' '))
        round.calculateMyWeapon()
        match round.play():
            case Outcome.WIN:
                score += Outcome.WIN.value
            case Outcome.DRAW:
                score += Outcome.DRAW.value
            case Outcome.LOSE:
                score += Outcome.LOSE.value
        score += round.p2Weapon.value + 1

    return score

main()
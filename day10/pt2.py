def main():
    with open('input11.txt') as f:
        drawCRTScreen(f)
        # print(strengthSignals)
        # print(sum(strengthSignals.values()))

    f.closed

def drawCRTScreen(f):
    crtScreen = ['' for i in range(240)]
    cycle = 0
    x = 1
    
    for line in f:
        instruction = line.split()
        if instruction[0] == 'addx':
            cycle += 1
            drawPixel(cycle, x, crtScreen)
            cycle += 1
            drawPixel(cycle, x, crtScreen)
            x += int(instruction[1])
        elif instruction[0] == 'noop':
            cycle += 1
            drawPixel(cycle, x, crtScreen)

    printCRTScreen(crtScreen)
    print(x)
    return crtScreen
        

def drawPixel(cycle, x, crtScreen):
    # print('cycle:' + str(cycle))
    # print('x:' + str(x))
    if (cycle-1)%40 == x-1 or (cycle-1)%40 == x or (cycle-1)%40 == x+1:
        crtScreen[cycle-1] = '#'
    else:
        crtScreen[cycle-1] = '.'


def printCRTScreen(crtScreen):
    # print(crtScreen)
    for i in range(6):
        print(''.join(crtScreen[40*i:40*(i+1)]))

main()
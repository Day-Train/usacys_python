#!/usr/bin/env python3

import random

def write_pgm(filename,content):
    with open(filename,'w') as fp:
        for p in content[0]:
            fp.write('{}\n'.format(p))
        for p in content[1]:
            fp.write('{} '.format(p))

def drawPGMimage(allpoints):
    filename = 'bressemers.pgm'
    pass
    # Student Implementation
    maxx = sorted(allpoints)[-1][0]
    maxy = sorted(allpoints, key=lambda x: x[1])[-1][1]
    pixels = []
    for y in range(maxy + 1):
        rowlist = []
        for x in range(maxx + 1):
            rowlist.append(0xff)
        pixels.append(rowlist)
    for point in allpoints:
        col = point[0]
        row = maxy - point[1]
        pixels[row][col] = 0x0
    pixelvalues = []
    for row in pixels:
        for col in row:
            pixelvalues.append(col)
    content = (['P2', '{}'.format(maxx+1), '{}'.format(maxy+1), 255], pixelvalues)
    write_pgm(filename,content)
    
def plot(x, y, allpoints=None):
    print('{},{}'.format(x, y))
    if allpoints != None:
        allpoints.append((x,y))

def plotLineLow(x0,y0, x1,y1, allpoints=None):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0
    for x in range(x0, x1+1):
        plot(x,y, allpoints)
        if D > 0:
            y = y + yi
            D = D - 2*dx
        D = D + 2*dy

def plotLineHigh(x0,y0, x1,y1, allpoints=None):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0

    for y in range(y0, y1+1):
        plot(x,y, allpoints)
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx


def plotLine(x0,y0, x1,y1, allpoints=None):
    allpoints = []
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0, allpoints)
        else:
            plotLineLow(x0, y0, x1, y1, allpoints)
    else:
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0, allpoints)
        else:
            plotLineHigh(x0, y0, x1, y1, allpoints)
    drawPGMimage(allpoints)



def drawline(x0, y0, x1, y1):
    # Student Implementation

    plotLine(x0,y0, x1,y1)
    return 0


if __name__ == '__main__':
    x0 = random.randint(0, 151)
    y0 = random.randint(0, 151)
    x1 = random.randint(0, 151)
    y1 = random.randint(0, 151)
    drawline(x0, y0, x1, y1)


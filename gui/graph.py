from mine import *
from pyfiglet import *

class Column(object):

    GAP = 3

    def __init__(self, height, width, colour, label):
        self.height = int(height)
        self.width = int(width)
        self.colour = colour
        self.label = label



class Graph(object):

    def __init__(self, mc, anchor, maxY, data):
        #TODO decide how this class is going to be used
        #TODO decide which of these are really object variables...

        self.data = data
        self.mc = mc
        self.anchor = anchor
        self.maxY = maxY


    def draw(self):
        self.buildAxes()


    def buildAxes(self):
        BIT_AT_THE_END = 2
        xLen = 0

        maxTextHeight = 0
        for i in self.data:
            colText = BlockText(self.mc, i.label)
            textLocation = Vec3(self.anchor.x+xLen, self.anchor.y, self.anchor.z)
            height = colText.writeText(textLocation)
            if height > maxTextHeight:
                maxTextHeight = height
            xLen = xLen + i.width + Column.GAP + BIT_AT_THE_END

        #adjust max height to sit axis above the text by 2 blocks
        maxTextHeight+=2
        xAxisYPos = maxTextHeight

        for j in range(xLen):
            self.mc.setBlock(self.anchor.x+j, self.anchor.y+maxTextHeight, self.anchor.z, 1)

        for k in range(self.maxY):
            self.mc.setBlock(self.anchor.x, self.anchor.y+k+maxTextHeight, self.anchor.z, 1)

        self.drawColumns(xAxisYPos)

#TODO - pass variables where not concerned with state of object, use member variables for state description


    def drawColumns(self, xAxisYPos):
        xAxisYPos += 1   #X axis margin
        textWidth = 7
        colIndex = 0

        for col in self.data:
            if colIndex == 0:
                gap = 0
                yAxisMargin = 1
            else:
                gap = Column.GAP
                yAxisMargin = 0

            #TODO there's an incorrect constant offset for cols > 0
            colXStart = self.anchor.x + yAxisMargin +\
                        (((textWidth + gap) - col.width) / 2) +\
                        (colIndex * (textWidth + gap))  #col 0 -> 0, col1 -> 8
            print(col.label)
            for j in range(col.height):
                for i in range(col.width):
                    #TODO centre each column in middle of txt width, which is 7 squares.
                    self.mc.setBlock(colXStart+i, self.anchor.y+xAxisYPos+j, self.anchor.z, col.colour)

            colIndex += 1

#TODO - figure out best way to implement all these for-loops

class BlockText(object):

    def __init__(self, mc, text, pos=None):
        self.text = text
        self.mc = mc
        self.pos = pos


    def writeText(self, pos):

        self.pos = Vec3(pos.x, pos.y, pos.z)  # new copy of the bar position.
        line = figlet_format(self.text, font='banner')
        listLine = line.rstrip().split('\n')  # split the result from 'figlet' into separate lines (right strip new line feeds)
        print("Text has been converted to:")
        print(line)

        print("starting pos = " + str(round(self.pos.x,2)) + ", " + str(round(self.pos.y,2)) + ", " + str(round(self.pos.z,2)))

        anchorX = self.pos.x
        anchorY = self.pos.y
        anchorZ = self.pos.z
        column = 0
        for row in listLine:
            anchorX += 1  # starting at top going down

            column = 0
            for letter in row:  # work along each row - check each character. If it's a '#' then print a block else leave it as air
                column += 1
                if letter == '#':
                    print("set block at:" + str(round(anchorX,2)) + ", " + str(round(anchorY+column,2)+column) + ", " + str(round(anchorZ,2)))
                    self.mc.setBlock(anchorX, anchorY+column, anchorZ, 1)

                else:
                    self.mc.setBlock(anchorX, anchorY+column, anchorZ, 0)

        return column


from mine import *

import calculator
from gui.graph import *
from portfolio import Portfolio


COLUMN_HEIGHT = 100
COLUMN_WIDTH = 1
COLUMN_GAP = 2
mc = Minecraft()

pos = mc.player.getTilePos()
prtf = Portfolio()
positions = prtf.getPositions()

columns = []
i = 0
for position in positions:
    column = Column(calculator.calcTotalValue(position), 5, Block(44 + i), position.getName)
    columns.append(column)
    i+=1

graph = Graph(mc, pos, 200, columns)

#TODO - make an offline mode, where some price is provided from config (for demo)

#TODO store player pos from first time, so that when we adjust height of columns, we can deal with
#absolute positions





        # polling_interval = 10
        # running= True b
        # while running:
        #    start = time.clock()
        #    poll_twitter()
        #    anything_else_that_seems_important()
        #    work_duration = time.clock() - start
        #    time.sleep( polling_interval - work_duration )


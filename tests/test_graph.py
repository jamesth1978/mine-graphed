import unittest
from mine import *

from gui.graph import *

class MyTest(unittest.TestCase):
    def testAxes(self):

        yAxisHeight = 200
        colWidth = 5

        mc = Minecraft()
        pos = mc.player.getPos()
        columns = []

        names = ["JAM.J", "MIL.J", "FLO.J", "ROO.J", "XTINA.J"]

        for i in range(len(names)):
            column = Column(10+(i*10), colWidth, Block(44 + i), names[i])
            columns.append(column)

        graph = Graph(mc, pos, yAxisHeight, columns)

        graph.buildAxes()




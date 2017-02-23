import unittest

from gui.graph import *

class TextTest(unittest.TestCase):
    def test(self):
        mc = Minecraft()
        pos = mc.player.getPos()

        mc.setBlock(pos,1)

        text = BlockText(mc, "VOD.L", pos)
        textHeight = text.writeText()
        print("text height: " + str(textHeight))
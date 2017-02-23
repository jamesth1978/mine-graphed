import unittest

from portfolio import Portfolio

class MyTest(unittest.TestCase):
    def test(self):
        prtf = Portfolio()

        print(str(prtf.getPositions()))
        self.assertTrue(len(prtf.getPositions())==10)


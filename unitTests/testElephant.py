import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.elephant import Elephant


class TestElephant(unittest.TestCase):
    def setUp(self):
        self.wElephant = Elephant(Canvas(), 100, 0, 100, "Elephant", "white", 2, 7)
        self.bElephant = Elephant(Canvas(), 100, 0, 100, "Elephant", "black", 5, 0)

        self.wChessBool = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, True,  False, False, False, False, False, False],
            [True,  False, False, True,  False, False, False, False],
            [False, False, True,  False, True,  True,  True,  True ],
            [True,  True,  True,  True,  True,  True,  True,  True ],
        ]
        self.bChessBool = [
            [True,  True,  True,  True,  True,  True,  True,  True ],
            [True,  True,  True,  True,  False, True,  False, False],
            [False, False, False, False, False, False, False, True ],
            [False, False, False, False, True,  False, True,  False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
        ]
        

    def testWElephantMovement(self):
        correctMovements = [[1, 6], [3, 6], [4, 5], [5, 4], [6, 3]]

        self.assertEqual(
            self.wElephant.calculateMovement(True, True, self.wChessBool, self.bChessBool),
            correctMovements
        )


    def testBElephantMovement(self):
        correctMovements = [[4, 1], [3, 2], [2, 3], [1, 4], [6, 1]]

        self.assertEqual(
            self.bElephant.calculateMovement(True, False, self.wChessBool, self.bChessBool),
            correctMovements
        )

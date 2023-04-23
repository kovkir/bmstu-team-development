import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.rook import Rook


class TestRook(unittest.TestCase):
    def setUp(self):
        self.wRook = Rook(Canvas(), 100, 0, 100, "Rook", "white", 0, 5)
        self.bRook = Rook(Canvas(), 100, 0, 100, "Rook", "black", 7, 4)

        self.wChessBool = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, True,  False, False],
            [True,  False, False, True,  False, False, False, False],
            [False, True,  True,  False, True,  False, True,  True ],
            [False, True,  True,  True,  True,  True,  True,  True ],
        ]
        self.bChessBool = [
            [True,  True,  True,  True,  True,  True,  True,  False],
            [True,  True,  True,  True,  True,  True,  True,  False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, True ],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
        ]
    
    
    def testWRookMovement(self):
        correctMovements = [[0, 4], [0, 3], [0, 2], [0, 1], [1, 5], [2, 5], [0, 6], [0, 7]]

        self.assertEqual(
            self.wRook.calculateMovement(True, True, self.wChessBool, self.bChessBool),
            correctMovements
        )

    
    def testBRookMovement(self):
        correctMovements = [[7, 3], [7, 2], [7, 1], [7, 0], [7, 5], [7, 6], [6, 4], [5, 4]]

        self.assertEqual(
            self.bRook.calculateMovement(True, False, self.wChessBool, self.bChessBool),
            correctMovements
        )

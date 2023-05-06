import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.queen import Queen


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.wQueen = Queen(Canvas(), 100, 0, 100, "Queen", "white", 3, 7)
        self.bQueen = Queen(Canvas(), 100, 0, 100, "Queen", "black", 3, 0)

        self.wChessBool = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, True,  False, False, False, False],
            [False, False, True,  False, False, True,  False, False],
            [True,  True,  False, False, False, False, True,  True ],
            [True,  True,  True,  True,  True,  True,  True,  True ],
        ]
        self.bChessBool = [
            [True,  True,  True,  True,  True,  True,  True,  True ],
            [True,  False, False, False, False, False, True,  True ],
            [False, True,  True,  False, True,  True,  False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
        ]


    def testWQueenMovement(self):
        correctMovements = [[3, 6], [3, 5], [2, 6], [1, 5], [0, 4], [4, 6]]

        self.assertEqual(
            self.wQueen.calculateMovement(True, True, self.wChessBool, self.bChessBool),
            correctMovements
        )

    
    def testBQueenMovement(self):
        correctMovements = [[3, 1], [3, 2], [3, 3], [3, 4], [2, 1], [4, 1]]

        self.assertEqual(
            self.bQueen.calculateMovement(True, False, self.wChessBool, self.bChessBool),
            correctMovements
        )

import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.king import King


class TestKing(unittest.TestCase):
    def setUp(self):
        self.wKing = King(Canvas(), 100, 0, 100, "King", "white", 4, 7)
        self.bKing = King(Canvas(), 100, 0, 100, "King", "black", 4, 0)

        self.wChessBool = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, True,  False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, True,  False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [True,  True,  True,  False, True,  False, True,  True ],
            [True,  True,  True,  True,  True,  True,  True,  True ],
        ]
        self.bChessBool = [
            [True,  True,  True,  True,  True,  True,  True,  True ],
            [True,  True,  True,  False, False, False, True,  True ],
            [False, False, False, False, False, False, False, False],
            [False, False, False, True,  False, True,  False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
        ]


    def testWKingMovement(self):
        correctMovements = [[3, 6], [5, 6]]

        self.assertEqual(
            self.wKing.calculateMovement(True, True, self.wChessBool, self.bChessBool),
            correctMovements
        )


    def testBKingMovement(self):
        correctMovements = [[3, 1], [4, 1], [5, 1]]

        self.assertEqual(
            self.bKing.calculateMovement(True, False, self.wChessBool, self.bChessBool),
            correctMovements
        )

import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.pawn import Pawn


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.wPawn = Pawn(Canvas(), 100, 0, 100, "Pawn", "white", 1, 6)
        self.bPawn = Pawn(Canvas(), 100, 0, 100, "Pawn", "black", 6, 1)

        self.wChessBool = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, True ],
            [False, False, False, False, False, False, True,  False],
            [False, False, False, False, False, False, False, False],
            [True,  False, False, False, False, False, False, False],
            [False, True,  True,  True,  True,  True,  False, False],
            [True,  True,  True,  True,  True,  True,  True,  True ],
        ]
        self.bChessBool = [
            [True,  True,  True,  True,  True,  True,  True,  True ],
            [True,  True,  True,  True,  True,  True,  True,  True ],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
        ]


    def testWPawnMovement(self):
        correctMovements = [[1, 5], [1, 4]]

        self.assertEqual(
            self.wPawn.calculateMovement(True, True, self.wChessBool, self.bChessBool),
            correctMovements
        )

    
    def testBPawnMovement(self):
        correctMovements = [[7, 2], [6, 2]]

        self.assertEqual(
            self.bPawn.calculateMovement(True, False, self.wChessBool, self.bChessBool),
            correctMovements
        )

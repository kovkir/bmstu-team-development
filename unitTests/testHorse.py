import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.horse import Horse


class TestHorse(unittest.TestCase):
    def setUp(self):
        self.wHorse = Horse(Canvas(), 100, 0, 100, "Horse", "white", 1, 7)
        self.bHorse = Horse(Canvas(), 100, 0, 100, "Horse", "black", 6, 0)

        self.wChessBool = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, True,  True,  False, False, False, False],
            [True,  True,  False, False, True,  True,  True,  True ],
            [True,  True,  True,  True,  True,  True,  True,  True ],
        ]
        self.bChessBool = [
            [True,  True,  True,  True,  True,  True,  True,  True ],
            [False, True,  True,  True,  True,  True,  True,  True ],
            [False, False, False, False, True,  False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [True,  False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
        ]


    def testWHorseMovement(self):
        correctMovements = [[0, 5], [3, 6]]

        self.assertEqual(
            self.wHorse.calculateMovement(True, True, self.wChessBool, self.bChessBool),
            correctMovements
        )


    def testBHorseMovement(self):
        correctMovements = [[7, 2], [5, 2]]

        self.assertEqual(
            self.bHorse.calculateMovement(True, False, self.wChessBool, self.bChessBool),
            correctMovements
        )

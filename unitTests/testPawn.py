import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.pawn import Pawn


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.wPawn = Pawn(Canvas(), 100, 0, 100, "Pawn", "white", 0, 6)
        self.bPawn = Pawn(Canvas(), 100, 0, 100, "Pawn", "black", 7, 1)


    def testWPawnMovement(self):
        movement = [[-1, 5], [0, 5], [1, 5], [0, 4]]
        self.assertEqual(self.wPawn.calculateMovement(True, True), movement)

    
    def testBPawnMovement(self):
        movement = [[6, 0], [7, 0], [8, 0], [7, -1]]
        self.assertEqual(self.bPawn.calculateMovement(True, True), movement)

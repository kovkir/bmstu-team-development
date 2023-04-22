import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.elephant import Elephant


class TestElephant(unittest.TestCase):
    def setUp(self):
        self.wElephant = Elephant(Canvas(), 100, 0, 100, "Elephant", "white", 2, 7)
        self.bElephant = Elephant(Canvas(), 100, 0, 100, "Elephant", "black", 5, 0)
        

    def testWElephantMovement(self):
        movement = [[1, 6], [0, 5], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2]]
        self.assertEqual(self.wElephant.calculateMovement(True, True), movement)


    def testBElephantMovement(self):
        movement = [[4, 1], [3, 2], [2, 3], [1, 4], [0, 5], [6, 1], [7, 2]]
        self.assertEqual(self.bElephant.calculateMovement(True, True), movement)

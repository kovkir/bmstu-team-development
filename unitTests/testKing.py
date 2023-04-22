import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.king import King


class TestKing(unittest.TestCase):
    def setUp(self):
        self.wKing = King(Canvas(), 100, 0, 100, "King", "white", 4, 7)
        self.bKing = King(Canvas(), 100, 0, 100, "King", "black", 4, 0)


    def testWKingMovement(self):
        movement = [[3, 8], [3, 6], [4, 8], [4, 6], [5, 8], [5, 6], [5, 7], [3, 7]]
        self.assertEqual(self.wKing.calculateMovement(True, True), movement)


    def testBKingMovement(self):
        movement = [[3, 1], [3, -1], [4, 1], [4, -1], [5, 1], [5, -1], [5, 0], [3, 0]]
        self.assertEqual(self.bKing.calculateMovement(True, True), movement)

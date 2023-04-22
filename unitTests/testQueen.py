import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.queen import Queen


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.wQueen = Queen(Canvas(), 100, 0, 100, "Queen", "white", 3, 7)
        self.bQueen = Queen(Canvas(), 100, 0, 100, "Queen", "black", 3, 0)


    def testWQueenMovement(self):
        movement = [[3, 0], [0, 7], [3, 1], [1, 7], [3, 2], [2, 7], [3, 3],
                    [3, 4], [4, 7], [3, 5], [5, 7], [3, 6], [6, 7], [7, 7],
                    [2, 6], [1, 5], [0, 4], [4, 6], [5, 5], [6, 4], [7, 3]]
        
        self.assertEqual(self.wQueen.calculateMovement(True, True), movement)

    
    def testBQueenMovement(self):
        movement = [[0, 0], [3, 1], [1, 0], [3, 2], [2, 0], [3, 3], [3, 4],
                    [4, 0], [3, 5], [5, 0], [3, 6], [6, 0], [3, 7], [7, 0], 
                    [2, 1], [1, 2], [0, 3], [4, 1], [5, 2], [6, 3], [7, 4]]
        
        self.assertEqual(self.bQueen.calculateMovement(True, True), movement)

import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.rook import Rook


class TestRook(unittest.TestCase):
    def setUp(self):
        self.wRook = Rook(Canvas(), 100, 0, 100, "Rook", "white", 0, 7)
        self.bRook = Rook(Canvas(), 100, 0, 100, "Rook", "black", 7, 0)
        
    
    def testWRookMovement(self):
        movement = [[0, 0], [0, 1], [1, 7], [0, 2], [2, 7], [0, 3], [3, 7], 
                    [0, 4], [4, 7], [0, 5], [5, 7], [0, 6], [6, 7], [7, 7]]
        
        self.assertEqual(self.wRook.calculateMovement(True, True), movement)

    
    def testBRookMovement(self):
        movement = [[0, 0], [7, 1], [1, 0], [7, 2], [2, 0], [7, 3], [3, 0],
                    [7, 4], [4, 0], [7, 5], [5, 0], [7, 6], [6, 0], [7, 7]]
        
        self.assertEqual(self.bRook.calculateMovement(True, True), movement)

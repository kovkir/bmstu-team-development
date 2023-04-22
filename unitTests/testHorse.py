import unittest
from tkinter import Canvas

import sys
sys.path.append("../src")
from chessPieces.horse import Horse


class TestHorse(unittest.TestCase):
    def setUp(self):
        self.wHorse = Horse(Canvas(), 100, 0, 100, "Horse", "white", 1, 7)
        self.bHorse = Horse(Canvas(), 100, 0, 100, "Horse", "black", 6, 0)


    def testWHorseMovement(self):
        movement = [[2, 5], [0, 5], [3, 6], [-1, 6], [2, 9], [0, 9], [3, 8], [-1, 8]]
        self.assertEqual(self.wHorse.calculateMovement(True, True), movement)


    def testBHorseMovement(self):
        movement = [[7, -2], [5, -2], [8, -1], [4, -1], [7, 2], [5, 2], [8, 1], [4, 1]]
        self.assertEqual(self.bHorse.calculateMovement(True, True), movement)

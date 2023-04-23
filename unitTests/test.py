import unittest

import os
os.system("Xvfb :1 -screen 0 720x720x16 &")
os.environ['DISPLAY'] = ":1.0"

from testElephant import TestElephant
from testHorse import TestHorse
from testKing import TestKing
from testPawn import TestPawn
from testQueen import TestQueen
from testRook import TestRook


if __name__ == "__main__":
    unittest.main()

# python3 test.py -v

import unittest
import math

def getNumLen(num: int) -> int:
    len = 1
    while num > 9:
        print(num)
        num = math.floor(num / 10)
        len += 1
    return len

class getNumLenUT(unittest.TestCase):
    def tests(self):
        self.assertEqual(getNumLen(0), 1)
        self.assertEqual(getNumLen(9), 1)
        self.assertEqual(getNumLen(10), 2)
        self.assertEqual(getNumLen(11), 2)
        self.assertEqual(getNumLen(890), 3)
        self.assertEqual(getNumLen(4000), 4)
        self.assertEqual(getNumLen(4432), 4)
        self.assertEqual(getNumLen(9999999), 7)
        self.assertEqual(getNumLen(4030), 4)
        self.assertEqual(getNumLen(333), 3)

if __name__ == '__main__':
    unittest.main()

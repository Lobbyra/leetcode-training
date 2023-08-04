import math
import unittest

def numRev(num: int) -> int:
    negFlag: int = 1
    if num < 0:
        negFlag = -1
        num *= -1
    newNum: int = 0
    while num != 0:
        print(f"newNum : {newNum}")
        print(f"num : {num}")
        newNum = (newNum * 10) + num % 10
        num = math.floor(num / 10)
    print(f"newNum : {newNum}")
    print(f"num : {num}")
    print("-------------------")
    return newNum * negFlag

class getNumLenUT(unittest.TestCase):
    def tests(self):
        self.assertEqual(numRev(0), 0)
        self.assertEqual(numRev(5), 5)
        self.assertEqual(numRev(9), 9)
        self.assertEqual(numRev(10), 1)
        self.assertEqual(numRev(909), 909)
        self.assertEqual(numRev(123), 321)
        self.assertEqual(numRev(2736), 6372)

if __name__ == '__main__':
    unittest.main()
